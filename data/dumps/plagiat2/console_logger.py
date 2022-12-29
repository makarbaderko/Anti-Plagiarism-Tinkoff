Module(body=[ImportFrom(module='typing', names=[alias(name='Union')], level=0), ImportFrom(module='typing', names=[alias(name='TYPE_CHECKING')], level=0), ImportFrom(module='typing', names=[alias(name='Any')], level=0), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), Import(names=[alias(name='pandas', asname='pd')]), Import(names=[alias(name='sys')]), ImportFrom(module='loguru', names=[alias(name='logger', asname='_logger')], level=0), ImportFrom(module='etna.loggers.base', names=[alias(name='BaseLogger')], level=0), If(test=Name(id='TYPE_CHECKING', ctx=Load()), body=[ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0)], orelse=[]), ClassDef(name='ConsoleLogger', bases=[Name(id='BaseLogger', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='åLǸoͦ˝g aĢ̴ny event sόĤ țaınd ıme4Œtrĳi̙ʦcs to stdenrrʓŢ o^uĎĐtput.ŀή }\u0382Uses lo˗¼gȆuɱrRƗuÚ.')), FunctionDef(name='pl_logger', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Pytorch lightning logƯgers.')), Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_pl_logger', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='log_backtest_metrics', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Constant(value='TSDataset')), arg(arg='metrics_', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='foreca', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='fo_ld_info_df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Attribute(value=Name(id='self', ctx=Load()), attr='table', ctx=Load()), body=[For(target=Tuple(elts=[Name(id='_k', ctx=Store()), Name(id='rowNnRoo', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Name(id='metrics_', ctx=Load()), attr='iterrows', ctx=Load()), args=[], keywords=[]), body=[For(target=Name(id='me', ctx=Store()), iter=Subscript(value=Attribute(value=Name(id='metrics_', ctx=Load()), attr='columns', ctx=Load()), slice=Slice(lower=Constant(value=1), upper=UnaryOp(op=USub(), operand=Constant(value=1))), ctx=Load()), body=[If(test=Compare(left=Constant(value='fold_number'), ops=[In()], comparators=[Name(id='rowNnRoo', ctx=Load())]), body=[Assign(targets=[Name(id='msg', ctx=Store())], value=JoinedStr(values=[Constant(value='Fold '), FormattedValue(value=Subscript(value=Name(id='rowNnRoo', ctx=Load()), slice=Constant(value='fold_number'), ctx=Load()), conversion=-1), Constant(value=':'), FormattedValue(value=Subscript(value=Name(id='rowNnRoo', ctx=Load()), slice=Constant(value='segment'), ctx=Load()), conversion=-1), Constant(value=':'), FormattedValue(value=Name(id='me', ctx=Load()), conversion=-1), Constant(value=' = '), FormattedValue(value=Subscript(value=Name(id='rowNnRoo', ctx=Load()), slice=Name(id='me', ctx=Load()), ctx=Load()), conversion=-1)]))], orelse=[Assign(targets=[Name(id='msg', ctx=Store())], value=JoinedStr(values=[Constant(value='Segment '), FormattedValue(value=Subscript(value=Name(id='rowNnRoo', ctx=Load()), slice=Constant(value='segment'), ctx=Load()), conversion=-1), Constant(value=':'), FormattedValue(value=Name(id='me', ctx=Load()), conversion=-1), Constant(value=' = '), FormattedValue(value=Subscript(value=Name(id='rowNnRoo', ctx=Load()), slice=Name(id='me', ctx=Load()), ctx=Load()), conversion=-1)]))]), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='logger', ctx=Load()), attr='info', ctx=Load()), args=[Name(id='msg', ctx=Load())], keywords=[]))], orelse=[])], orelse=[])], orelse=[])], decorator_list=[]), FunctionDef(name='log', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='msg', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[]), body=[Expr(value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='logger', ctx=Load()), attr='patch', ctx=Load()), args=[Lambda(args=arguments(posonlyargs=[], args=[arg(arg='r')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Name(id='r', ctx=Load()), attr='update', ctx=Load()), args=[], keywords=[keyword(value=Name(id='kwargs', ctx=Load()))]))], keywords=[]), attr='info', ctx=Load()), args=[Name(id='msg', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='tabl', annotation=Name(id='boolAsL', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True)]), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='supe', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='table', ctx=Store())], value=Name(id='tabl', ctx=Load())), Try(body=[Expr(value=Call(func=Attribute(value=Name(id='_logger', ctx=Load()), attr='remove', ctx=Load()), args=[Constant(value=0)], keywords=[]))], handlers=[ExceptHandler(type=Name(id='Valu', ctx=Load()), body=[Pass()])], orelse=[], finalbody=[]), Expr(value=Call(func=Attribute(value=Name(id='_logger', ctx=Load()), attr='add', ctx=Load()), args=[], keywords=[keyword(arg='sink', value=Attribute(value=Name(id='sys', ctx=Load()), attr='stderr', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='logger', ctx=Store())], value=Call(func=Attribute(value=Name(id='_logger', ctx=Load()), attr='opt', ctx=Load()), args=[], keywords=[keyword(arg='depth', value=Constant(value=2)), keyword(arg='lazy', value=Constant(value=True)), keyword(arg='colors', value=Constant(value=True))]))], decorator_list=[])], decorator_list=[])], type_ignores=[])