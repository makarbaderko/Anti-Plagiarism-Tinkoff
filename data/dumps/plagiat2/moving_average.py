Module(body=[ImportFrom(module='etna.models.seasonal_ma', names=[alias(name='SeasonalMovingAverageModel')], level=0), ClassDef(name='MovingAverageModel', bases=[Name(id='SeasonalMovingAverageModel', ctx=Load())], keywords=[], body=[FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='window', annotation=Name(id='i', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=5)]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='window', ctx=Store())], value=Name(id='window', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='window', value=Name(id='window', ctx=Load())), keyword(arg='seasonality', value=Constant(value=1))]))], decorator_list=[])], decorator_list=[]), Assign(targets=[Name(id='__all__', ctx=Store())], value=List(elts=[Constant(value='MovingAverageModel')], ctx=Load()))], type_ignores=[])