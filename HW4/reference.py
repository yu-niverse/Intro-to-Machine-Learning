def cross_validation(x_train, y_train, k=5):
    ret = []
    mod, l = len(x_train) % k, int(len(x_train) / k)
    arr = np.arange(len(x_train))
    np.random.shuffle(arr)
    for i in range(k):
        if mod > 0:
            ret.append([np.concatenate((arr[:i], arr[i+l+1:]), axis=0), arr[i:i+l+1]])
            i += l + 1
        else:
            ret.append([np.concatenate((arr[:i], arr[i+l:]), axis=0), arr[i:i+l]])  
            i += l
        mod -= 1
    return ret
    