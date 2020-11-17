def nearest_square(num):

    """Function to calculate nearest square of any number.

        Args: 
            num (int): Any integer

        Returns: 
            Int: Nearest Square of num
        """

    answer = 0
    while (answer+1)**2 < num:
        answer += 1
    return answer**2