import numpy as np
import scipy.optimize as sco

def voting_bloc_scoring (x, weights, smoothing):
    rows = np.zeros(weights.shape[0])
    blocs = int(x.shape[0]/weights.shape[0])
    func = 0
    grad = np.zeros(x.shape)
    gradmat = np.zeros((x.shape[0],weights.shape[0]))
    for i in range(weights.shape[0]) :
        baseline = 0
        for j in range(weights.shape[1]) :
            u_dist = x[i*blocs:(i + 1)*blocs]
            v_dist = x[j*blocs:(j + 1)*blocs]
            baseline += (weights[i,j] * np.dot(u_dist,v_dist))
            for k in range(blocs):
                gradmat[i*blocs + k,i] += weights[i,j] * v_dist[k]
                gradmat[i*blocs + k,j] = weights[i,j] * v_dist[k]
        rows[i] = np.exp(baseline/smoothing)
    grad = np.dot(gradmat,rows)
    func = np.log(np.sum(rows)/weights.shape[0]) * smoothing
    return (func, grad)

def voting_bloc_jac (x, weights, smoothing):
    blocs = int(x.shape[0]/weights.shape[0])
    grad = np.zeros(x.shape)
    for i in range(weights.shape[0]):
        for j in range(blocs):
            v_divs = x[j::blocs]
            grad[i*blocs + j] = np.dot(weights[i],v_divs)
    return grad

def voting_bloc_hess (x,weights, smoothing):
    blocs = int(x.shape[0]/weights.shape[0])
    hess_base =  np.kron(weights,np.identity(blocs))
    return hess_base
    hess_base += np.kron(np.diagflat(np.sum(weights,0)),np.identity(blocs))
    return hess_base

def optimize_scoring (weights, blocs, smoothing = 10, verbose = False):
    x0 = np.random.randint(1, 100, (weights.shape[0] * blocs))
#    x0 = np.zeros((weights.shape[0] * blocs))
    for i in range(weights.shape[0]) :
#        x0[i*blocs] = 1
       x0[i*blocs : (i + 1)*blocs] = x0[i * blocs : (i + 1) * blocs] / np.sum(x0[i*blocs : (i+1)*blocs])

    lb = np.full(x0.shape,0)
    ub = np.full(x0.shape,1)
    dist_bounds = sco.Bounds(lb,ub)
    dist_sum = np.kron(np.identity(weights.shape[0]),np.ones((blocs)))
    dist_constr = sco.LinearConstraint(dist_sum,np.ones((weights.shape[0])),np.ones((weights.shape[0])))
    opti_result = sco.minimize(fun = voting_bloc_scoring,x0 = x0,args = (weights, smoothing),method = 'trust-constr',
                               jac = True, hess = '3-point',
                               bounds = dist_bounds, constraints = dist_constr,
                               options = {'disp': verbose})
    if opti_result.success:
        print ("Optimized to score:", opti_result.fun)
        print ("Optimized gradient:", opti_result.grad)
        opti_dist = opti_result.x
        opti_dict = np.zeros((weights.shape[0]))
        for i in range(weights.shape[0]):
            for j in range(blocs):
                if opti_dist[i*blocs + j] > 0.5:
                    opti_dict[i] = j
        return opti_dict
    else:
        print ("Optimization failure")
        return np.full((weights.shape[0]),1)
    

