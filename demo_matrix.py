from hopfield_network import HopfieldNetwork

hn = HopfieldNetwork(4)
hn.train([-1, 1, 1, 1])

hn.present([-1, 1, 1, 1])
hn.present([-1, -1, 1, 1])
hn.present([-1, -1, -1, 1])
hn.present([-1, -1, -1, -1])
