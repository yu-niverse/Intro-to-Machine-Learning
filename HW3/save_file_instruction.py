import pickle

'''
    First,
    Train your model and name It as "my_model"
    Do the prediction and name it as y_pred
    
    Then,
    add the following code to save your model and prediction,
    and email the following files to me!
        1. the two file (one .pickle and one .npy)
        2. your training code (.ipynb)
'''

with open('model.pickle', 'wb') as pkl_file:
    pickle.dump(my_model, pkl_file, protocol=pickle.HIGHEST_PROTOCOL)

np.save("y_pred.npy", y_pred)

