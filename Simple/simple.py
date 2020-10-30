from random import randrange


class Simple:
    def iniciar(self):
        result = self.get_list(5)
        order_result = self.order_list(result)

        print (("%s%s%s%s%s%s" % (order_result, "\n",
                                  "El id de la edad menor es: %i" % order_result[0]['id'], "\n",
                                  "El id de la edad mayor es: %i" % order_result[len(result) - 1]['id'], "\n")))

    def get_list(self, n_element):
        """
               Return a list of dictionary in the specific range with the parameter n_element
               >>> s = Simple()
               >>> s.get_list('a')
               Traceback (most recent call last):
               ......
               ValueError: invalid literal for int() with base 10: 'a'
               >>> s = Simple()
               >>> s.get_list(1)[0]['id']
               0

               """
        list_element = []
        for i in range(0, int(n_element)):
            list_element.append({'id': i,
                                 'edad': randrange(1, 100)})

        return list_element

    def order_list(self, list_element):
        """
               This function order the list and return the minor and max values
               >>> s = Simple()
               >>> s.order_list([{'id:0, edad:45'},{'id:1, edad:37'},{'id:2, edad:15'},{'id:3, edad:2'}])
               [{'id:3, edad:2'},{'id:2, edad:15'},{'id:1, edad:37'},{'id:0, edad:45'}]
               """
        order = sorted(list_element)
        return order

#import doctest
#doctest.testmod()

Simple().iniciar()