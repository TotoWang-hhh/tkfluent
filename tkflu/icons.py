def icon():
    from tempfile import mkstemp

    _icon = b"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"

    _, _temp = mkstemp()

    with open(_temp, "wb") as _file:
        from base64 import b64decode

        _file.write(b64decode(_icon))

    _icon2 = (_temp).replace("\\", "//")

    return _icon2


def light():
    from tempfile import mkstemp

    _icon = b"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"

    _, _temp = mkstemp()

    with open(_temp, "wb") as _file:
        from base64 import b64decode

        _file.write(b64decode(_icon))

    _icon2 = (_temp).replace("\\", "//")

    return _icon2

def dark():
    from tempfile import mkstemp
    _icon = b"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAABMlJREFUWEe1l1msXmMUhp9lnucYY455iHmMmIIEF2Yxz1wQwg2XLrhyITEFVTEmokqookoMV4a2iPRCq+ZS89yKSD/f06x9srv773P+U/XdnOHf/7fetdb7vmvtYDlOKWVVYA1gNWAxsCgi/lqOq4jxfqmUsjawM3AosBvwM/A68E5E/DHe+8YFoJSyJnAwcCqwCfA78Gv+nAe8FhELxgNiaACllLWAA4GzgN1rBaYBT2cbzgQOq+BerJ89GRFfDQtiKAAZfD/gfGCXDD4Z+BTYATgXuARYGbgXmBAR3w4DYkwAGXzfDLCtZQYm1b8/B7YAzgDOAbYG1gO+Ax4F7ogIfx/1jAoge27Zzdzgb1pi4DNgS+BswPL72d+AbdoQ+BJ4yGpExNejIegFkMEPyp7vCrwKPBURc1IJpwBX1mrsAfwJrAKsk5xQot8DdwokIgQ08AwEkGU/IDM0gIQz+NxSitrfH7gipagsDe7P1YFfAPvfAHowOTGwEssAaPX8otrLHYFXDF7b8DGwUsrw0lSEPReQmRv8N/0AeBb4sXrEdcD22Y67BnFiKQAttl+cpHojCWdwzxHAeZl5E7zJ3ODvJljlqD8cC9xUAWxXgTycxFxKHSMAWj2X0Wauu03Kniuvw5Ptgmh63QQ32IwMPl0fyGSOB66p5D2m8sUWTKiJTWz7RJRSBOFFsl1JaTLTW4SzxPLBlgiiL7i+8JKsL6WsW+V6JGCrJPLGOTvMXmI+0hBTAJJFb9dIDPRyi3AOHf93WV7ULXuTucFf0IYzczP2O/sAmwJaeFNtveHurMYCAfihvToqpfNMEq6kvcoHs2gHV2bOAQknQc38m1TIiekbOudmneCNFOdXH7nfaghA47g+WTyxkmxuPuWk02jU+/qAgCyt7XL0akYSS++37FZLeVrJk9KQBKpyBp2pVaq3CMD+3Ax4we0R8VHyQgASUqfzGUuo0/mcY/eTBDA5Iua3ANj3kyvjN0qJ9pndlHrXrQIwqwuSYB8C9nNeRCwupRxXtX1DEspWWQUv/Key+4dsgS2b1mqB2ds2uSNwSdwFoUc8UKt5mwDMaM/80t4dEm4OnF65cTWgHbcvEoSEmgk8V1U0NUHYIjl1VTUkh1i3EjqlSSrJWUsuTG9XhpZ7RIY5bp1y8sDeCrR9BGE7PgAeTxCNDI9Ou3aB2SBb5/YkaZ2WMyNi4VhG5ORz5m+VQ8mpaJW6Z2G64GMuJckJ+XICcG0qzLJr0U7JGRGxyEuGtWIZ7+xXFRfmBOz2VWW8lZWQYFqzrbgxd8fns+zvmXmTwbDDqFlA3AHkxOW5GXUlJoi3K1+eSH44jNygnA32/P128GUq0KDqG8cdTghCvnSPu4GW64Ji7w3uSJ7VDd4LIImp7LoLiZVQ/9sAp+V82KvHaGyBz2tWIz3vPrsiVjLHc5eYX2QbZPzsQZn3cqCLsGcpVR3NUqp0nZQ6p4PNlbyZ/f9tKe1wor2WL5mYOQ9cNqyCK5p7wz1VMfetsLW8A6L9YiK5fDFxFVOevqr9Py8mLRAS85A6Axy5zgXZLtOdqG5EmtBQLyRDc2AAJ9yIfA9w2XRjduDMrqN4SkT81KOI3n+P+WY0AIDf0YCsxk7Z9zkRoezGff4FJEWot2oJkhgAAAAASUVORK5CYII="

    _, _temp = mkstemp()

    with open(_temp, "wb") as _file:
        from base64 import b64decode

        _file.write(b64decode(_icon))

    _icon2 = (_temp).replace("\\", "//")

    return _icon2