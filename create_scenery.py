from random import randint

import person
import obstacle
import common
import config
import check


def floor(floor_y):

    for i in range(1, common.cols+1):
        if (common.value_arr(i, floor_y) == " "):
            common.set_arr(i, floor_y, "0")
            common.set_arr(i, floor_y+1, "0")


def create_floor():
    floor(common.mids_r+1)


def create_Enemy():

    if (randint(0, 20) == 5):
        try:
            check.check_life(common.cols-1, common.mids_r, "Enemy")
            e = person.Enemy(common.cols-1, common.mids_r)
            config.e_list.append(e)
        except (config.Enemy_Here, config.Gap_Here):
            pass

    for i in config.e_list:
        try:
            i.move(i.x-1, i.y)
        except config.Wall_Here:
            pass
        except config.Enemy_Here:
            config.e_list.remove(i)


def create_Mario():
    config.m = person.Mario(common.r3, common.mids_r)


def create_Wall():
    if len(config.w_list) == 0:
        pos = randint(config.m.x+4, common.r2)
        if common.value_arr(pos, common.mids_r) == " " and common.value_arr(pos, common.mids_r+1) == "0":
            try:
                w = obstacle.Wall(pos)
                config.w_list.append(w)
            except config.Gap_Here:
                pass

    elif len(config.w_list) < int((3*common.cols)/80):
        if (randint(0, 10) == 5):
            # create a obstacle
            pos = config.w_list[-1].x + randint(10, 20)
            if pos < common.cols - 3:
                try:
                    w = obstacle.Wall(pos)
                    config.w_list.append(w)
                except config.Gap_Here:
                    pass

    else:
        pass


def create_Platform():

    if len(config.p_list) == 0:
        p = obstacle.Platform(
            randint(config.m.x+2, common.cols-5), randint(2, common.mids_r-5))
        config.p_list.append(p)
    elif len(config.p_list) < int(common.cols/20):
        if(randint(0, 5) == 1):
            pos = config.p_list[-1].x + randint(7, 15)
            if pos < (common.cols - 3):
                p = obstacle.Platform(pos, randint(0, common.mids_r-5))
                config.p_list.append(p)

    for i in config.p_list:
        x = randint(-1, 1)+i.x
        i.move(i.x)


def create_Gap():

    if config.g_list == []:
        g = obstacle.Gap(randint(config.m.x + 2, common.cols-2))
        config.g_list.append(g)
    elif(randint(0, 10) == 1):
        g = obstacle.Gap(randint(config.m.x + 2, common.cols-2))
        config.g_list.append(g)


def create_Marijuana():

    if len(config.m_list) == 0:
        try:
            m = obstacle.Marijuana(randint(common.mids, common.cols-1))
            config.m_list.append(m)
        except (config.Dead_Mario, config.Wall_Here):
            pass
    elif len(config.m_list) <= max(len(config.w_list), int(common.cols/20)):
        pos = config.m_list[-1].x + randint(5, 10)
        if(randint(0, 10) == 1 and pos < common.cols-3):
            try:
                m = obstacle.Marijuana(pos)
                config.m_list.append(m)
            except (config.Dead_Mario, config.Wall_Here):
                pass


def check_floor():
    print("vsd")
    if common.value_arr(config.m.x, config.m.y+1) != "0":
        while(common.value_arr(config.m.x, config.m.y+1) != "0"):
            config.m.move(config.m.x, config.m.y+1)


def create_scene():
    create_floor()
    if config.m != "":
        create_Wall()
        create_Enemy()
        create_Gap()
        create_Platform()
        create_Marijuana()
