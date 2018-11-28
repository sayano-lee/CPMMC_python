import numpy as np

def CCCP_MMC_dual(**kwargs):

    omega_0 = kwargs['omega_0']
    b_0 = kwargs['b_0']
    xi_0 = kwargs['xi_0']
    C = kwargs['C']
    W = kwargs['W']
    l = kwargs['l']
    data = kwargs['data'].transpose()

    constraint_dim, data_dim = W.shape[0], W.shape[1]
    dim, tmp = omega_0.shape[0], omega_0.shape[1]

    # omega_old = omega_0
    # b_old = b_0
    # xi_old = xi

    f_val = 0.5 * omega_0.transpose() * omega_0 + C * xi_0

    continue_flag = True
    per_quit = 0.01

    iter = 0
    c_k = W.mean(axis=1)
    # s_k = np.zeros((constraint_dim, 1))
    # z_k = np.zeros((dim, constraint_dim))
    x_k = np.sum(data, axis=1)[:,np.newaxis]

    while(continue_flag):
        tmp_z_k = np.zeros((dim, data_dim))
        tmp_s_k = np.zeros((data_dim, 1))

        for i in range(data_dim):
            tmp_s_k[i] = np.sign(omega_0.transpose().dot(data[:,i][:,np.newaxis])+b_0)
            tmp_z_k[:,i] = tmp_s_k[i] * data[:,i]

        s_k = W.dot(tmp_s_k) / data_dim
        z_k = tmp_z_k.dot(W.transpose()) / data_dim

        # import ipdb
        # ipdb.set_trace()
        x_mat = np.concatenate((z_k, -x_k, x_k), axis=1)
        HQP = x_mat.transpose().dot(x_mat)
        fQP = [-c_k, l, l]

        import ipdb
        ipdb.set_trace()
        inter = np.ones((1, constraint_dim))
        AQP = np.append((inter, [0, 0]), axis=0)
        bQP = C

        Aeq = [-s_k.transpose(), data_dim, -data_dim]
        beq = 0

        import ipdb
        ipdb.set_trace()
