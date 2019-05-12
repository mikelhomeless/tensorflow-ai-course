tensorflow version used - 2.0.0-alpha0
python version - 3.6 (3.7 is incompatible )

My code uses TensorFlow's Keras to get the neural network set up.

Numerical columns: 'age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'slope', 'ca'
categorical columns (uses one-hot): sex, cp, restecg, thal, fbs

Network configurations tried:
  3 layers
    - 128 nodes, linear
    - 128 nodes, linear
    - 1 node, softmax (as was recommended)

  3 layers
    - 128 nodes, relu
    - 128 nodes, linear
    - 1 node, softmax

  3 layers
    - 128 nodes, relu
    - 128 nodes, relu
    - 1 node, softmax

  3 layers
    - 128 nodes, relu
    - 128 nodes, sigmoid
    - 1 node, softmax

  3 layers
    - 128 nodes, sigmoid
    - 128 nodes, sigmoid
    - 1 node, softmax

  4 layers
    - 128 nodes, relu
    - 128 nodes, relu
    - 32 nodes, linear
    - 1 node, softmax

  4 layers
    - 128 nodes, relu
    - 128 nodes, linear
    - 32 nodes, sigmoid
    - 1 node, softmax

  5 layers
    - 128 nodes, relu
    - 128 nodes, linear
    - 32 nodes, sigmoid
    - 64 nodes, linear
    - 1 node, softmax

  BEST
  5 layers
    - 128 nodes, sigmoid
    - 128 nodes, sigmoid
    - 32 nodes, relu
    - 25 nodes, relu
    - 1 node, softmax

What made this the best outcome: ¯\\\_(ツ)\_/¯
  My best guess is that, having the sigmoid functions at the beginning of the network help to categorize the data
  from the start of each pass (since that's what sigmoid functions are best for). Then having the Relu functions at
  the end help to drop off data that don't meet a specific threshold.

  The best runs usually had a sigmoid funtion at the start
