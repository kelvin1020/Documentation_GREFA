#!/usr/bin/env python
"""
An example of how to use bilby to perform parameter estimation for
non-gravitational wave data. In this case, fitting a linear function to
data with background Gaussian noise
举例说明如何使用bilby对非引力波数据进行参数估计。在本例中，对背景为高斯噪声的数据拟合一个线性函数

"""
import bilby
import numpy as np
import matplotlib.pyplot as plt

# A few simple setup steps 
# 一些简单的设置步骤

label = 'linear_regression'
outdir = 'outdir'
bilby.utils.check_directory_exists_and_if_not_mkdir(outdir)


# First, we define our "signal model", in this case a simple linear function
# 首先，我们定义我们的“信号模型”，在这个例子中是一个简单的线性函数

def model(time, m, c):
    return time * m + c


# Now we define the injection parameters which we make simulated data with
# 现在我们定义注入参数，我们用它来模拟数据

injection_parameters = dict(m=0.5, c=0.2)

# For this example, we'll use standard Gaussian noise
# 在这个例子中，我们将使用标准高斯噪声

# These lines of code generate the fake data. Note the ** just unpacks the
# contents of the injection_parameters when calling the model function.
#这些代码行生成假数据。注意**只是在调用模型函数时解包injection_parameters的内容。

sampling_frequency = 10
time_duration = 10
time = np.arange(0, time_duration, 1 / sampling_frequency)
N = len(time)
sigma = np.random.normal(1, 0.01, N)
data = model(time, **injection_parameters) + np.random.normal(0, sigma, N)

# We quickly plot the data to check it looks sensible
#我们快速绘制数据，检查它是否合理

fig, ax = plt.subplots()
ax.plot(time, data, 'o', label='data')
ax.plot(time, model(time, **injection_parameters), '--r', label='signal')
ax.set_xlabel('time')
ax.set_ylabel('y')
ax.legend()
fig.savefig('{}/{}_data.png'.format(outdir, label))

# Now lets instantiate a version of our GaussianLikelihood, giving it
# the time, data and signal model
#现在让我们实例化一个版本的GaussianLikelihood，给它时间，数据和信号模型

likelihood = bilby.likelihood.GaussianLikelihood(time, data, model, sigma)

# From hereon, the syntax is exactly equivalent to other bilby examples
# We make a prior
#从这里开始，语法完全等同于其他bilby示例
#我们设置一个先验分布

priors = dict()
priors['m'] = bilby.core.prior.Uniform(0, 5, 'm')
priors['c'] = bilby.core.prior.Uniform(-2, 2, 'c')

# And run sampler
# 并且运行采样器

result = bilby.run_sampler(
    likelihood=likelihood, priors=priors, sampler='dynesty', nlive=500,
    sample='unif', injection_parameters=injection_parameters, outdir=outdir,
    label=label)
result.plot_corner()
