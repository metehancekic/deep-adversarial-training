"""
Hyper-parameters
"""
import argparse


def get_arguments():
    """ Hyper-parameters """

    parser = argparse.ArgumentParser(description="PyTorch CIFAR10")

    # Directory
    parser.add_argument("--directory", type=str, default="/home/metehan/deep_adv/CIFAR10/",
                        metavar="", help="Directory of experiments",
                        )

    neural_net = parser.add_argument_group("neural_net", "Neural Network arguments")

    # Neural Model
    neural_net.add_argument("--model", type=str, default="ResNet", metavar="ResNet",
                            help="Which model to use",
                            )

    # Optimizer
    neural_net.add_argument("--lr", type=float, default=0.1, metavar="LR", help="Learning rate",
                            )
    neural_net.add_argument("--lr_min", type=float, default=0., metavar="LR",
                            help="Learning rate min",
                            )
    neural_net.add_argument("--lr_max", type=float, default=0.2, metavar="LR",
                            help="Learning rate max",
                            )
    neural_net.add_argument("--momentum", type=float, default=0.9, metavar="M",
                            help="Optimizer momentum",
                            )
    neural_net.add_argument("--weight_decay", type=float, default=0.0005, metavar="WD",
                            help="Weight decay",
                            )

    # Batch Sizes & #Epochs
    neural_net.add_argument("--batch_size", type=int, default=128, metavar="N",
                            help="Batch size for train",
                            )
    neural_net.add_argument("--test_batch_size", type=int, default=200, metavar="N",
                            help="Batch size for test",
                            )
    neural_net.add_argument("--epochs", type=int, default=15, metavar="N",
                            help="Number of epochs",
                            )
    # Adversarial training parameters
    adv_training = parser.add_argument_group("adv_training", "Adversarial training arguments")

    adv_training.add_argument("-tra", "--tr_attack", type=str, default="fgsm", metavar="fgsm/pgd",
                              help="Attack method",
                              )
    adv_training.add_argument("--tr_norm", type=str, default="inf", metavar="inf/p",
                              help="Attack norm",
                              )
    adv_training.add_argument("-tr_eps", "--tr_epsilon", type=float, default=(8.0/255.0),
                              metavar="", help="attack budget",
                              )
    adv_training.add_argument("-tr_a", "--tr_alpha", type=float, default=(10.0/255.0),
                              metavar="", help="random fgsm budget",
                              )
    adv_training.add_argument("-tr_Ss", "--tr_step_size", type=float, default=(2.0/255.0),
                              metavar="", help="Step size for PGD, adv training",
                              )
    adv_training.add_argument("-tr_Ni", "--tr_num_iterations", type=int, default=10,
                              metavar="", help="Number of iterations for PGD, adv training",
                              )
    adv_training.add_argument("--tr_rand", action="store_false", default=True,
                              help="randomly initialize attack for training",
                              )
    adv_training.add_argument("-tr_Nrest", "--tr_num_restarts", type=int, default=1, metavar="",
                              help="number of restarts for pgd for training",
                              )

    # Adversarial testing parameters
    adv_testing = parser.add_argument_group("adv_testing", "Adversarial testing arguments")

    adv_testing.add_argument("--attack", type=str, default="pgd", metavar="fgsm/pgd",
                             help="Attack method",
                             )
    adv_testing.add_argument("--norm", type=str, default="inf", metavar="inf/p",
                             help="Which attack norm to use",
                             )
    adv_testing.add_argument("-eps", "--epsilon", type=float, default=(8.0/255.0), metavar="",
                             help="attack budget",
                             )
    adv_testing.add_argument("-Ss", "--step_size", type=float, default=(2.0/255.0), metavar="",
                             help="Step size for PGD",
                             )
    adv_testing.add_argument("-Ni", "--num_iterations", type=int, default=20, metavar="",
                             help="Number of iterations for PGD",
                             )
    adv_testing.add_argument("--rand", action="store_true", default=False,
                             help="randomly initialize PGD attack",
                             )
    adv_testing.add_argument("-Nrest", "--num_restarts", type=int, default=1, metavar="",
                             help="number of restarts for pgd",
                             )

    # Others
    others = parser.add_argument_group("others", "Other arguments")

    others.add_argument("--no-cuda", action="store_true", default=False,
                        help="disables CUDA training"
                        )
    others.add_argument("--seed", type=int, default=1, metavar="S",
                        help="random seed (default: 1)"
                        )
    others.add_argument("--log-interval", type=int, default=100, metavar="N",
                        help="how many batches to wait before logging training status",
                        )

    # Actions
    actions = parser.add_argument_group("actions", "Action arguments")

    actions.add_argument("-tr", "--train", action="store_true",
                         help="Train network, default = False"
                         )
    actions.add_argument("-at", "--attack_network", action="store_true",
                         help="Attack network, default = False",
                         )
    actions.add_argument("-bb", "--black_box", action="store_true",
                         help="Attack network, default = False",
                         )
    actions.add_argument("-sm", "--save-model", action="store_true", default=False,
                         help="For Saving the current Model, default = False ",
                         )
    # actions.add_argument('-im', '--initialize-model', action='store_false', default=True,
    #                      help='Init the model from checkpoint with standard parameters'
    #                      )

    apex_amp = parser.add_argument_group("apex_amp", "Apex module arguments")
    apex_amp.add_argument('--opt_level', default='O2', type=str, choices=['O0', 'O1', 'O2'],
                          help='O0 is do nothing, O1 is Mixed Precision(MP), O2 is "Almost FP16" MP'
                          )
    apex_amp.add_argument('--loss_scale', default='1.0', type=str, choices=['1.0', 'dynamic'],
                          help='If "dynamic", adaptively adjust the loss scale over time'
                          )
    apex_amp.add_argument('--master_weights', action='store_true',
                          help='Maintain FP32 master weights to accompany any FP16 model weights.'
                          )

    args = parser.parse_args()

    return args
