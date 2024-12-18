for i in range(1, 13):
    print("No. {0:^2} squared is {1:<3} and cubed is {2:<4}"
          .format(i, i ** 2, i ** 3))


    print(f"No. %d squared is %d and cubed is %d", i, i ** 2, i ** 3)
    print(f"> No.  {i}" + f"squared is {i ** 2} " + f"and cubed is {i ** 3}")
