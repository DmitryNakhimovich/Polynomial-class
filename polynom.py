class Polynomial(object):

    # constructor
    def __init__(self, args):
        "args equal to variable power by reverse order: [3, 2, 1] = 3X2 + 2X + 1"
        self.coeffs = []
        self.correct = True
        self.degree = 0

        if isinstance(args, Polynomial):
            self.coeffs = args.coeffs[:]
        elif isinstance(args, list):
            for el in args:
                if not isinstance(el, (int, float)):
                    self.correct = False
                    raise TypeError('Bad parameters in Polynomial constructor', el, args)
            if self.correct:
                if not args:
                    self.coeffs = [0]
                else:
                    self.coeffs = args
        elif isinstance(args, (int, float)):
            self.coeffs.append(args)
        else:
            self.correct = False
            raise TypeError('Bad parameters in Polynomial constructor', args, args)

        self.__trim()

    # deleting 0 trailing coeffs
    def __trim(self):
        if self.coeffs and self.correct:
            while len(self.coeffs) > 1 and self.coeffs[0] == 0:
                self.coeffs.pop(0)
        self.degree = len(self.coeffs) - 1 if len(self.coeffs) >= 1 else 0

    # return str
    def __str__(self):
        "Return string formatted as aXb : a - value of parameter, b - power, x - variable"
        # Example: [3, -5, 1, -1] = 3x^3-4x^2+x-1
        res = []
        for power, coeff in enumerate(self.coeffs):
            if coeff:
                if power == 0:
                    if len(self.coeffs) > 2:
                        power = 'x^' + str(len(self.coeffs) - 1 - power)
                        if abs(coeff) != 1:
                            res.append(('-' + str(abs(coeff)) if coeff < 0 else '' + str(coeff)) + power)
                        else:
                            res.append(('-' if coeff < 0 else '') + power)
                    elif len(self.coeffs) == 2:
                        power = 'x'
                        if abs(coeff) != 1:
                            res.append(('-' + str(abs(coeff)) if coeff < 0 else '' + str(coeff)) + power)
                        else:
                            res.append(('-' if coeff < 0 else '') + power)
                    elif len(self.coeffs) == 1:
                        power = ''
                        res.append(('-' + str(abs(coeff)) if coeff < 0 else '' + str(coeff)) + power)
                elif power == len(self.coeffs) - 2:
                    power = 'x'
                    if abs(coeff) != 1:
                        res.append(('-' + str(abs(coeff)) if coeff < 0 else '+' + str(coeff)) + power)
                    else:
                        res.append(('-' if coeff < 0 else '+') + power)
                elif power == len(self.coeffs) - 1:
                    power = ''
                    res.append(('-' + str(abs(coeff)) if coeff < 0 else '+' + str(coeff)) + power)
                else:
                    power = 'x^' + str(len(self.coeffs) - 1 - power)
                    if abs(coeff) != 1:
                        res.append(('-' + str(abs(coeff)) if coeff < 0 else '+' + str(coeff)) + power)
                    else:
                        res.append(('-' if coeff < 0 else '+') + power)
        if res:
            return ''.join(res)
        else:
            return "0"

    # p == q
    def __eq__(self, arg):
        if isinstance(arg, Polynomial):
            return self.coeffs == arg.coeffs
        elif isinstance(arg, (int, float)):
            return len(self.coeffs) == 1 and self.coeffs[0] == arg
        else:
            return False

    # p != q
    def __ne__(self, arg):
        return not self == arg

    # p + q
    def __add__(self, arg):
        res = []
        offset = 0
        if isinstance(arg, Polynomial):
            if self.degree > arg.degree:
                offset = self.degree - arg.degree
                res = self.coeffs[:]
                for i in range(0, arg.degree + 1, 1):
                    res[i + offset] += arg.coeffs[i]
            else:
                offset = arg.degree - self.degree
                res = arg.coeffs[:]
                for i in range(0, self.degree + 1, 1):
                    res[i + offset] += self.coeffs[i]
        elif isinstance(arg, (int, float)):
            if self.coeffs:
                res = self.coeffs[:]
                res[-1] += arg
            else:
                res = arg
        else:
            raise TypeError('Bad arg in Polynomial add function', arg)
        return Polynomial(res)

    # q + p
    def __radd__(self, arg):
        return self + arg

    # -p
    def __neg__(self):
        return Polynomial([-coeff for coeff in self.coeffs])

    # p - q
    def __sub__(self, arg):
        if isinstance(arg, (int, float, Polynomial)):
            return self.__add__(-arg)
        else:
            raise TypeError('Bad arg in Polynomial sub function', arg)

    # q - p
    def __rsub__(self, arg):
        if isinstance(arg, (int, float, Polynomial)):
            return (self.__neg__()).__add__(arg)
        else:
            raise TypeError('Bad arg in Polynomial sub function', arg)

    # p * q
    def __mul__(self, arg):
        res = []
        if isinstance(arg, Polynomial):
            res = [0] * (self.degree + arg.degree + 1)
            for self_power, self_coeff in enumerate(self.coeffs):
                for arg_pow, arg_coeff in enumerate(arg.coeffs):
                    res[self_power + arg_pow] += self_coeff * arg_coeff
        elif isinstance(arg, (int, float)):
            res = [coeff * arg for coeff in self.coeffs]
        else:
            raise TypeError('Bad arg in Polynomial mul function', arg)
        return Polynomial(res)

    # q * p
    def __rmul__(self, arg):
        return self * arg
