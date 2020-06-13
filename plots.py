import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(4, 1, figsize=(20, 30))


def draw_membership(members, name, i):
    r = []

    for loc, range in members.items():
        ax[i].plot(range[0], range[1], label=loc)
        r = np.concatenate([r, range[0]])
    ax[i].set_yticks([0, 1])
    ax[i].legend()
    ax[i].grid(True)
    ax[i].set_title(name)
    ax[i].set_xticks(r)


if __name__ == '__main__':

    theta = {'down_left': ([315, 360],
                           [0, 1]),

             'left': ([220, 290, 320],
                      [0, 1, 0]),

             'top_left': ([180, 195, 235],
                          [0, 1, 0]),

             'middle': ([170, 180, 190],
                        [0, 1, 0]),

             'top_right': ([125, 165, 180],
                           [0, 1, 0]),

             'right': ([40, 70, 140],
                       [0, 1, 0]),

             'down_right': ([0, 45],
                            [1, 0])}

    theta_dot = {'cw_fast': ([3, 7],
                             [0, 1]),

                 'cw_medium': ([1, 3, 6.5],
                               [0, 1, 0]),

                 'cw': ([0, 1, 3],
                        [0, 1, 0]),

                 'fix': ([-0.15, 0, 0.15],
                         [0, 1, 0]),

                 'acw': ([-3, -1, 0],
                         [0, 1, 0]),

                 'acw_medium': ([-1, -3, -6.5],
                                [0, 1, 0]),

                 'acw_fast': ([-7, -3],
                              [1, 0])}

    x_dot = {'fast_left': ([-80, -60],
                           [1, 0]),

             'slow_left': ([-60, -40, 0],
                           [0, 1, 0]),

             'static': ([-40, 0, 40],
                        [0, 1, 0]),

             'slow_right': ([0, 40, 60],
                            [0, 1, 0]),

             'fast_right': ([60, 80],
                            [0, 1])}

    F = {'left_very_fast': ([-80, -60], [1, 0]),

         'left_fast': ([-80, -70, -50],
                       [0, 1, 0]),

         'left_medium': ([-60, -50, -20],
                         [0, 1, 0]),

         'left': ([-50, -20, 0],
                  [0, 1, 0]),

         'fix': ([-0.4, 0, 0.4],
                 [0, 1, 0]),

         'right': ([0, 20, 50],
                   [0, 1, 0]),

         'right_medium': ([20, 50, 60],
                          [0, 1, 0]),

         'right_fast': ([50, 70,80],
                        [0, 1,0]),

         'right_very_fast': ([60, 80],
                            [0, 1])}

    draw_membership(theta, 'theta', 0)
    draw_membership(theta_dot, 'theta_dot', 1)
    draw_membership(x_dot, 'x_dot', 2)
    draw_membership(F, 'F', 3)
    plt.savefig('memberships.png')
    plt.show()
