def compose(F, G):
    def FG(X, Z):
        Y = G(X)
        return F(Y, Z)
    return FG