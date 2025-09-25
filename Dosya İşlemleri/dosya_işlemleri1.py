class File():
    def __init__(self):


        class file():
            def __init__(self):
                with open("nfjhfj","r",encoding="utf-8") as file:
                    print(file.tell())
                    file.seek()

                    with open("mrje","")
        with open("C:\\Users\\DELL\\Desktop\\METİN.txt","r",encoding="utf-16") as file:
            text=file.read()
            world=text.split()

            self.clean_world=list()

            for i in world:
                i=i.strip("\n")
                i=i.strip()
                i=i.strip(".")
                i=i.strip(",")

                self.clean_world.append(i)
    def all_world(self):
        clean_world=set(self.clean_world)

        print("All world.........")

        for i in clean_world:
            print(i)
            print("*******************************")

    def world_frekans(self):
        world_dict=dict()

        for i in self.clean_world:
            if (i in world_dict):
                world_dict[i] += 1
            else:
                world_dict[i] = 1
        for world,howTimes in world_dict.items():
            print("{} kelimesi {} defa geçiyor....".format(world,howTimes))
            print("*******************************")


file=File()
file.all_world()
file.world_frekans()


