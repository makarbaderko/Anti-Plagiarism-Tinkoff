Module(body=[Import(names=[alias(name='argparse')]), Import(names=[alias(name='re')]), Import(names=[alias(name='sys')]), Import(names=[alias(name='wandb')]), FunctionDef(name='parse_arguments', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='parser', ctx=Store())], value=Call(func=Attribute(value=Name(id='argparse', ctx=Load()), attr='ArgumentParser', ctx=Load()), args=[Constant(value='Download metrics from WandB.')], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='parser', ctx=Load()), attr='add_argument', ctx=Load()), args=[Constant(value='wandb_path')], keywords=[keyword(arg='help', value=Constant(value="Path to the project in format 'entity/project'."))])), Expr(value=Call(func=Attribute(value=Name(id='parser', ctx=Load()), attr='add_argument', ctx=Load()), args=[Constant(value='-f'), Constant(value='--filename')], keywords=[keyword(arg='help', value=Constant(value='Dump output to file.'))])), Expr(value=Call(func=Attribute(value=Name(id='parser', ctx=Load()), attr='add_argument', ctx=Load()), args=[Constant(value='--group')], keywords=[keyword(arg='help', value=Constant(value="Group to load metrics from (use '-' to match ungrouped runs)."))])), Expr(value=Call(func=Attribute(value=Name(id='parser', ctx=Load()), attr='add_argument', ctx=Load()), args=[Constant(value='--run-regexp')], keywords=[keyword(arg='nargs', value=Constant(value='*')), keyword(arg='help', value=Constant(value='Regexp to filter runs.'))])), Expr(value=Call(func=Attribute(value=Name(id='parser', ctx=Load()), attr='add_argument', ctx=Load()), args=[Constant(value='--metric-regexp')], keywords=[keyword(arg='nargs', value=Constant(value='*')), keyword(arg='help', value=Constant(value='Regexp to filter metrics.'))])), Expr(value=Call(func=Attribute(value=Name(id='parser', ctx=Load()), attr='add_argument', ctx=Load()), args=[Constant(value='--percent')], keywords=[keyword(arg='help', value=Constant(value='Multiply metrics by 100.')), keyword(arg='action', value=Constant(value='store_true'))])), Expr(value=Call(func=Attribute(value=Name(id='parser', ctx=Load()), attr='add_argument', ctx=Load()), args=[Constant(value='--precision')], keywords=[keyword(arg='help', value=Constant(value='Number of decimal places.')), keyword(arg='type', value=Name(id='int', ctx=Load())), keyword(arg='default', value=Constant(value=2))])), Expr(value=Call(func=Attribute(value=Name(id='parser', ctx=Load()), attr='add_argument', ctx=Load()), args=[Constant(value='--separator')], keywords=[keyword(arg='help', value=Constant(value='Fields separator.')), keyword(arg='default', value=Constant(value=' '))])), Expr(value=Call(func=Attribute(value=Name(id='parser', ctx=Load()), attr='add_argument', ctx=Load()), args=[Constant(value='--url')], keywords=[keyword(arg='help', value=Constant(value='WandB URL.')), keyword(arg='default', value=Constant(value='https://api.wandb.ai'))])), Return(value=Call(func=Attribute(value=Name(id='parser', ctx=Load()), attr='parse_args', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), FunctionDef(name='matches', args=arguments(posonlyargs=[], args=[arg(arg='s'), arg(arg='regexps')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[For(target=Name(id='regexp', ctx=Store()), iter=Name(id='regexps', ctx=Load()), body=[If(test=Compare(left=Call(func=Attribute(value=Name(id='re', ctx=Load()), attr='search', ctx=Load()), args=[Name(id='regexp', ctx=Load()), Name(id='s', ctx=Load())], keywords=[]), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Return(value=Constant(value=True))], orelse=[])], orelse=[]), Return(value=Constant(value=False))], decorator_list=[]), FunctionDef(name='get_runs', args=arguments(posonlyargs=[], args=[arg(arg='api'), arg(arg='path'), arg(arg='group'), arg(arg='run_regexps')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None), Constant(value=None)]), body=[Assign(targets=[Name(id='runs', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[Call(func=Attribute(value=Name(id='api', ctx=Load()), attr='runs', ctx=Load()), args=[], keywords=[keyword(arg='path', value=Name(id='path', ctx=Load()))])], keywords=[])), If(test=Compare(left=Name(id='group', ctx=Load()), ops=[Eq()], comparators=[Constant(value='-')]), body=[Assign(targets=[Name(id='runs', ctx=Store())], value=ListComp(elt=Name(id='run', ctx=Load()), generators=[comprehension(target=Name(id='run', ctx=Store()), iter=Name(id='runs', ctx=Load()), ifs=[UnaryOp(op=Not(), operand=Attribute(value=Name(id='run', ctx=Load()), attr='group', ctx=Load()))], is_async=0)]))], orelse=[If(test=Compare(left=Name(id='group', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='runs', ctx=Store())], value=ListComp(elt=Name(id='run', ctx=Load()), generators=[comprehension(target=Name(id='run', ctx=Store()), iter=Name(id='runs', ctx=Load()), ifs=[BoolOp(op=And(), values=[Compare(left=Attribute(value=Name(id='run', ctx=Load()), attr='group', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), Call(func=Name(id='matches', ctx=Load()), args=[Attribute(value=Name(id='run', ctx=Load()), attr='group', ctx=Load()), List(elts=[Name(id='group', ctx=Load())], ctx=Load())], keywords=[])])], is_async=0)]))], orelse=[])]), If(test=Compare(left=Name(id='run_regexps', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='runs', ctx=Store())], value=ListComp(elt=Name(id='run', ctx=Load()), generators=[comprehension(target=Name(id='run', ctx=Store()), iter=Name(id='runs', ctx=Load()), ifs=[Call(func=Name(id='matches', ctx=Load()), args=[Attribute(value=Name(id='run', ctx=Load()), attr='name', ctx=Load()), Name(id='run_regexps', ctx=Load())], keywords=[])], is_async=0)]))], orelse=[]), Return(value=Name(id='runs', ctx=Load()))], decorator_list=[]), FunctionDef(name='get_metrics', args=arguments(posonlyargs=[], args=[arg(arg='run'), arg(arg='metric_regexps')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Assign(targets=[Name(id='metrics', ctx=Store())], value=Attribute(value=Name(id='run', ctx=Load()), attr='summary', ctx=Load())), If(test=Compare(left=Name(id='metric_regexps', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='metrics', ctx=Store())], value=DictComp(key=Name(id='k', ctx=Load()), value=Name(id='v', ctx=Load()), generators=[comprehension(target=Tuple(elts=[Name(id='k', ctx=Store()), Name(id='v', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Name(id='metrics', ctx=Load()), attr='items', ctx=Load()), args=[], keywords=[]), ifs=[Call(func=Name(id='matches', ctx=Load()), args=[Name(id='k', ctx=Load()), Name(id='metric_regexps', ctx=Load())], keywords=[])], is_async=0)]))], orelse=[]), Return(value=Name(id='metrics', ctx=Load()))], decorator_list=[]), FunctionDef(name='prepare_metric', args=arguments(posonlyargs=[], args=[arg(arg='metric'), arg(arg='percent'), arg(arg='precision')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=False), Constant(value=2)]), body=[If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='metric', ctx=Load()), Name(id='str', ctx=Load())], keywords=[]), body=[Return(value=Name(id='metric', ctx=Load()))], orelse=[]), If(test=Name(id='percent', ctx=Load()), body=[Assign(targets=[Name(id='metric', ctx=Store())], value=BinOp(left=Name(id='metric', ctx=Load()), op=Mult(), right=Constant(value=100)))], orelse=[]), Assign(targets=[Name(id='fmt', ctx=Store())], value=BinOp(left=BinOp(left=Constant(value='{:.'), op=Add(), right=Call(func=Name(id='str', ctx=Load()), args=[Name(id='precision', ctx=Load())], keywords=[])), op=Add(), right=Constant(value='f}'))), Return(value=Call(func=Attribute(value=Name(id='fmt', ctx=Load()), attr='format', ctx=Load()), args=[Name(id='metric', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='order_metrics', args=arguments(posonlyargs=[], args=[arg(arg='metrics'), arg(arg='metric_regexps')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Assign(targets=[Name(id='metrics', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Name(id='list', ctx=Load()), args=[Name(id='metrics', ctx=Load())], keywords=[])], keywords=[])], keywords=[])), If(test=Compare(left=Name(id='metric_regexps', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='ordered', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Name(id='regexp', ctx=Store()), iter=Name(id='metric_regexps', ctx=Load()), body=[For(target=Name(id='metric', ctx=Store()), iter=Name(id='metrics', ctx=Load()), body=[If(test=Compare(left=Name(id='metric', ctx=Load()), ops=[In()], comparators=[Name(id='ordered', ctx=Load())]), body=[Continue()], orelse=[]), If(test=Call(func=Name(id='matches', ctx=Load()), args=[Name(id='metric', ctx=Load()), List(elts=[Name(id='regexp', ctx=Load())], ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Attribute(value=Name(id='ordered', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='metric', ctx=Load())], keywords=[]))], orelse=[])], orelse=[])], orelse=[]), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='metrics', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='ordered', ctx=Load())], keywords=[])])), Assign(targets=[Name(id='metrics', ctx=Store())], value=Name(id='ordered', ctx=Load()))], orelse=[]), Return(value=Name(id='metrics', ctx=Load()))], decorator_list=[]), FunctionDef(name='print_metrics', args=arguments(posonlyargs=[], args=[arg(arg='fp'), arg(arg='metrics'), arg(arg='run_metrics'), arg(arg='separator'), arg(arg='percent'), arg(arg='precision')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=' '), Constant(value=False), Constant(value=2)]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Call(func=Attribute(value=Name(id='separator', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='metrics', ctx=Load())], keywords=[])], keywords=[keyword(arg='file', value=Name(id='fp', ctx=Load()))])), For(target=Name(id='run', ctx=Store()), iter=Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Name(id='list', ctx=Load()), args=[Name(id='run_metrics', ctx=Load())], keywords=[])], keywords=[]), body=[Assign(targets=[Name(id='tokens', ctx=Store())], value=BinOp(left=List(elts=[Name(id='run', ctx=Load())], ctx=Load()), op=Add(), right=ListComp(elt=Call(func=Name(id='prepare_metric', ctx=Load()), args=[Call(func=Attribute(value=Subscript(value=Name(id='run_metrics', ctx=Load()), slice=Name(id='run', ctx=Load()), ctx=Load()), attr='get', ctx=Load()), args=[Name(id='name', ctx=Load()), Constant(value='N/A')], keywords=[])], keywords=[keyword(arg='percent', value=Name(id='percent', ctx=Load())), keyword(arg='precision', value=Name(id='precision', ctx=Load()))]), generators=[comprehension(target=Name(id='name', ctx=Store()), iter=Name(id='metrics', ctx=Load()), ifs=[], is_async=0)]))), Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Call(func=Attribute(value=Name(id='separator', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='tokens', ctx=Load())], keywords=[])], keywords=[keyword(arg='file', value=Name(id='fp', ctx=Load()))]))], orelse=[])], decorator_list=[]), FunctionDef(name='main', args=arguments(posonlyargs=[], args=[arg(arg='args')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='entity', ctx=Store()), Name(id='project', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='args', ctx=Load()), attr='wandb_path', ctx=Load()), attr='split', ctx=Load()), args=[Constant(value='/')], keywords=[])), Assign(targets=[Name(id='api', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Attribute(value=Name(id='wandb', ctx=Load()), attr='apis', ctx=Load()), attr='public', ctx=Load()), attr='Api', ctx=Load()), args=[], keywords=[keyword(arg='overrides', value=Dict(keys=[Constant(value='base_url')], values=[Attribute(value=Name(id='args', ctx=Load()), attr='url', ctx=Load())]))])), Assign(targets=[Name(id='runs', ctx=Store())], value=Call(func=Name(id='get_runs', ctx=Load()), args=[Name(id='api', ctx=Load()), Call(func=Attribute(value=Constant(value='{}/{}'), attr='format', ctx=Load()), args=[Name(id='entity', ctx=Load()), Name(id='project', ctx=Load())], keywords=[])], keywords=[keyword(arg='group', value=Attribute(value=Name(id='args', ctx=Load()), attr='group', ctx=Load())), keyword(arg='run_regexps', value=Attribute(value=Name(id='args', ctx=Load()), attr='run_regexp', ctx=Load()))])), Assign(targets=[Name(id='metrics', ctx=Store())], value=DictComp(key=Attribute(value=Name(id='run', ctx=Load()), attr='name', ctx=Load()), value=Call(func=Name(id='get_metrics', ctx=Load()), args=[Name(id='run', ctx=Load())], keywords=[keyword(arg='metric_regexps', value=Attribute(value=Name(id='args', ctx=Load()), attr='metric_regexp', ctx=Load()))]), generators=[comprehension(target=Name(id='run', ctx=Store()), iter=Name(id='runs', ctx=Load()), ifs=[], is_async=0)])), Assign(targets=[Name(id='metrics_order', ctx=Store())], value=Call(func=Name(id='order_metrics', ctx=Load()), args=[Call(func=Name(id='set', ctx=Load()), args=[Call(func=Name(id='sum', ctx=Load()), args=[Call(func=Name(id='map', ctx=Load()), args=[Name(id='list', ctx=Load()), Call(func=Attribute(value=Name(id='metrics', ctx=Load()), attr='values', ctx=Load()), args=[], keywords=[])], keywords=[]), List(elts=[], ctx=Load())], keywords=[])], keywords=[])], keywords=[keyword(arg='metric_regexps', value=Attribute(value=Name(id='args', ctx=Load()), attr='metric_regexp', ctx=Load()))])), Assign(targets=[Name(id='print_kwargs', ctx=Store())], value=Dict(keys=[Constant(value='separator'), Constant(value='percent'), Constant(value='precision')], values=[Attribute(value=Name(id='args', ctx=Load()), attr='separator', ctx=Load()), Attribute(value=Name(id='args', ctx=Load()), attr='percent', ctx=Load()), Attribute(value=Name(id='args', ctx=Load()), attr='precision', ctx=Load())])), If(test=Compare(left=Attribute(value=Name(id='args', ctx=Load()), attr='filename', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[With(items=[withitem(context_expr=Call(func=Name(id='open', ctx=Load()), args=[Attribute(value=Name(id='args', ctx=Load()), attr='filename', ctx=Load()), Constant(value='w')], keywords=[]), optional_vars=Name(id='fp', ctx=Store()))], body=[Expr(value=Call(func=Name(id='print_metrics', ctx=Load()), args=[Name(id='fp', ctx=Load()), Name(id='metrics_order', ctx=Load()), Name(id='metrics', ctx=Load())], keywords=[keyword(value=Name(id='print_kwargs', ctx=Load()))]))])], orelse=[Expr(value=Call(func=Name(id='print_metrics', ctx=Load()), args=[Attribute(value=Name(id='sys', ctx=Load()), attr='stdout', ctx=Load()), Name(id='metrics_order', ctx=Load()), Name(id='metrics', ctx=Load())], keywords=[keyword(value=Name(id='print_kwargs', ctx=Load()))]))])], decorator_list=[]), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Assign(targets=[Name(id='args', ctx=Store())], value=Call(func=Name(id='parse_arguments', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Name(id='main', ctx=Load()), args=[Name(id='args', ctx=Load())], keywords=[]))], orelse=[])], type_ignores=[])