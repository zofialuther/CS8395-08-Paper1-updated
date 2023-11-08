from pyswip import Prolog

prolog = Prolog()

prolog.assertz("functor(Array,array,100)")
prolog.assertz("arg(1,Array,a)")
prolog.assertz("arg(12,Array,b)")
prolog.assertz("arg(1,Array,Value1)")
prolog.assertz("print(Value1),nl")
prolog.assertz("arg(4,Array,Value2)")
prolog.assertz("print(Value2),nl")

list(prolog.query("singleassignment."))