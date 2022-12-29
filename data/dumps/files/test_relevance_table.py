Module(body=[Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), Import(names=[alias(name='pytest')]), ImportFrom(module='sklearn.tree', names=[alias(name='DecisionTreeRegressor')], level=0), ImportFrom(module='etna.analysis.feature_relevance', names=[alias(name='get_model_relevance_table')], level=0), ImportFrom(module='etna.analysis.feature_relevance', names=[alias(name='get_statistics_relevance_table')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='duplicate_data')], level=0), FunctionDef(name='test_interface', args=arguments(posonlyargs=[], args=[arg(arg='method'), arg(arg='method_kwargs'), arg(arg='simple_df_relevance')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='df', ctx=Store()), Name(id='df_exog', ctx=Store())], ctx=Store())], value=Name(id='simple_df_relevance', ctx=Load())), Assign(targets=[Name(id='relevance_table', ctx=Store())], value=Call(func=Name(id='method', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load())), keyword(arg='df_exog', value=Name(id='df_exog', ctx=Load())), keyword(value=Name(id='method_kwargs', ctx=Load()))])), Assert(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='relevance_table', ctx=Load()), Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='sorted', ctx=Load()), args=[Attribute(value=Name(id='relevance_table', ctx=Load()), attr='index', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[])], keywords=[])])), Assert(test=Compare(left=Call(func=Name(id='sorted', ctx=Load()), args=[Attribute(value=Name(id='relevance_table', ctx=Load()), attr='columns', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='df_exog', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[])], keywords=[])]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='method,method_kwargs'), Tuple(elts=[Tuple(elts=[Name(id='get_statistics_relevance_table', ctx=Load()), Dict(keys=[], values=[])], ctx=Load()), Tuple(elts=[Name(id='get_model_relevance_table', ctx=Load()), Dict(keys=[Constant(value='model')], values=[Call(func=Name(id='DecisionTreeRegressor', ctx=Load()), args=[], keywords=[])])], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_statistics_relevance_table', args=arguments(posonlyargs=[], args=[arg(arg='simple_df_relevance')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='df', ctx=Store()), Name(id='df_exog', ctx=Store())], ctx=Store())], value=Name(id='simple_df_relevance', ctx=Load())), Assign(targets=[Name(id='relevance_table', ctx=Store())], value=Call(func=Name(id='get_statistics_relevance_table', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load())), keyword(arg='df_exog', value=Name(id='df_exog', ctx=Load()))])), Assert(test=Compare(left=Subscript(value=Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Constant(value='regressor_1'), ctx=Load()), slice=Constant(value='1'), ctx=Load()), ops=[Lt()], comparators=[Constant(value=1e-14)])), Assert(test=Compare(left=Subscript(value=Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Constant(value='regressor_1'), ctx=Load()), slice=Constant(value='2'), ctx=Load()), ops=[Gt()], comparators=[Constant(value=0.1)])), Assert(test=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='isnan', ctx=Load()), args=[Subscript(value=Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Constant(value='regressor_2'), ctx=Load()), slice=Constant(value='1'), ctx=Load())], keywords=[])), Assert(test=Compare(left=Subscript(value=Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Constant(value='regressor_2'), ctx=Load()), slice=Constant(value='2'), ctx=Load()), ops=[Lt()], comparators=[Constant(value=1e-10)]))], decorator_list=[]), FunctionDef(name='test_model_relevance_table', args=arguments(posonlyargs=[], args=[arg(arg='simple_df_relevance')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='df', ctx=Store()), Name(id='df_exog', ctx=Store())], ctx=Store())], value=Name(id='simple_df_relevance', ctx=Load())), Assign(targets=[Name(id='relevance_table', ctx=Store())], value=Call(func=Name(id='get_model_relevance_table', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load())), keyword(arg='df_exog', value=Name(id='df_exog', ctx=Load())), keyword(arg='model', value=Call(func=Name(id='DecisionTreeRegressor', ctx=Load()), args=[], keywords=[]))])), Assert(test=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='allclose', ctx=Load()), args=[Subscript(value=Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Constant(value='regressor_1'), ctx=Load()), slice=Constant(value='1'), ctx=Load()), Constant(value=1)], keywords=[])), Assert(test=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='allclose', ctx=Load()), args=[Subscript(value=Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Constant(value='regressor_2'), ctx=Load()), slice=Constant(value='1'), ctx=Load()), Constant(value=0)], keywords=[])), Assert(test=Compare(left=Subscript(value=Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Constant(value='regressor_1'), ctx=Load()), slice=Constant(value='2'), ctx=Load()), ops=[Lt()], comparators=[Subscript(value=Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Constant(value='regressor_2'), ctx=Load()), slice=Constant(value='2'), ctx=Load())]))], decorator_list=[]), FunctionDef(name='exog_and_target_dfs', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='seg', ctx=Store())], value=BinOp(left=BinOp(left=List(elts=[Constant(value='a')], ctx=Load()), op=Mult(), right=Constant(value=30)), op=Add(), right=BinOp(left=List(elts=[Constant(value='b')], ctx=Load()), op=Mult(), right=Constant(value=30)))), Assign(targets=[Name(id='time', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[Subscript(value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[Constant(value='2020-01-01'), Constant(value='2021-01-01')], keywords=[]), slice=Slice(upper=Constant(value=30)), ctx=Load())], keywords=[])), Assign(targets=[Name(id='timestamps', ctx=Store())], value=BinOp(left=Name(id='time', ctx=Load()), op=Mult(), right=Constant(value=2))), Assign(targets=[Name(id='target', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='arange', ctx=Load()), args=[Constant(value=60)], keywords=[])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='segment'), Constant(value='timestamp'), Constant(value='target')], values=[Name(id='seg', ctx=Load()), Name(id='timestamps', ctx=Load()), Name(id='target', ctx=Load())])], keywords=[])), Assign(targets=[Name(id='ts', ctx=Store())], value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Assign(targets=[Name(id='cast', ctx=Store())], value=BinOp(left=BinOp(left=BinOp(left=BinOp(left=List(elts=[Constant(value='1.1')], ctx=Load()), op=Mult(), right=Constant(value=10)), op=Add(), right=BinOp(left=List(elts=[Constant(value='2')], ctx=Load()), op=Mult(), right=Constant(value=9))), op=Add(), right=List(elts=[Constant(value=None)], ctx=Load())), op=Add(), right=BinOp(left=List(elts=[Constant(value='56.1')], ctx=Load()), op=Mult(), right=Constant(value=10)))), Assign(targets=[Name(id='no_cast', ctx=Store())], value=BinOp(left=BinOp(left=BinOp(left=List(elts=[Constant(value='1.1')], ctx=Load()), op=Mult(), right=Constant(value=10)), op=Add(), right=BinOp(left=List(elts=[Constant(value='two')], ctx=Load()), op=Mult(), right=Constant(value=10))), op=Add(), right=BinOp(left=List(elts=[Constant(value='56.1')], ctx=Load()), op=Mult(), right=Constant(value=10)))), Assign(targets=[Name(id='none', ctx=Store())], value=BinOp(left=BinOp(left=BinOp(left=List(elts=[Constant(value=1)], ctx=Load()), op=Mult(), right=Constant(value=10)), op=Add(), right=BinOp(left=List(elts=[Constant(value=2)], ctx=Load()), op=Mult(), right=Constant(value=10))), op=Add(), right=BinOp(left=List(elts=[Constant(value=56.1)], ctx=Load()), op=Mult(), right=Constant(value=10)))), Assign(targets=[Subscript(value=Name(id='none', ctx=Load()), slice=Constant(value=10), ctx=Store())], value=Constant(value=None)), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp'), Constant(value='exog1'), Constant(value='exog2'), Constant(value='exog3'), Constant(value='cast'), Constant(value='no_cast'), Constant(value='none')], values=[Name(id='time', ctx=Load()), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='arange', ctx=Load()), args=[Constant(value=100), Constant(value=70), UnaryOp(op=USub(), operand=Constant(value=1))], keywords=[]), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='sin', ctx=Load()), args=[BinOp(left=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='arange', ctx=Load()), args=[Constant(value=30)], keywords=[]), op=Div(), right=Constant(value=10))], keywords=[]), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='exp', ctx=Load()), args=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='arange', ctx=Load()), args=[Constant(value=30)], keywords=[])], keywords=[]), Name(id='cast', ctx=Load()), Name(id='no_cast', ctx=Load()), Name(id='none', ctx=Load())])], keywords=[])), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='cast'), ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='cast'), ctx=Load()), attr='astype', ctx=Load()), args=[Constant(value='category')], keywords=[])), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='no_cast'), ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='no_cast'), ctx=Load()), attr='astype', ctx=Load()), args=[Constant(value='category')], keywords=[])), Assign(targets=[Name(id='df_exog', ctx=Store())], value=Call(func=Name(id='duplicate_data', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[keyword(arg='segments', value=List(elts=[Constant(value='a'), Constant(value='b')], ctx=Load()))])), Return(value=Tuple(elts=[Name(id='ts', ctx=Load()), Name(id='df_exog', ctx=Load())], ctx=Load()))], decorator_list=[Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load()), args=[], keywords=[])]), FunctionDef(name='exog_and_target_dfs_with_none', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='seg', ctx=Store())], value=BinOp(left=BinOp(left=List(elts=[Constant(value='a')], ctx=Load()), op=Mult(), right=Constant(value=30)), op=Add(), right=BinOp(left=List(elts=[Constant(value='b')], ctx=Load()), op=Mult(), right=Constant(value=30)))), Assign(targets=[Name(id='time', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[Subscript(value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[Constant(value='2020-01-01'), Constant(value='2021-01-01')], keywords=[]), slice=Slice(upper=Constant(value=30)), ctx=Load())], keywords=[])), Assign(targets=[Name(id='timestamps', ctx=Store())], value=BinOp(left=Name(id='time', ctx=Load()), op=Mult(), right=Constant(value=2))), Assign(targets=[Name(id='target', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='arange', ctx=Load()), args=[Constant(value=60)], keywords=[keyword(arg='dtype', value=Name(id='float', ctx=Load()))])), Assign(targets=[Subscript(value=Name(id='target', ctx=Load()), slice=Constant(value=5), ctx=Store())], value=Attribute(value=Name(id='np', ctx=Load()), attr='nan', ctx=Load())), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='segment'), Constant(value='timestamp'), Constant(value='target')], values=[Name(id='seg', ctx=Load()), Name(id='timestamps', ctx=Load()), Name(id='target', ctx=Load())])], keywords=[])), Assign(targets=[Name(id='ts', ctx=Store())], value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Assign(targets=[Name(id='none', ctx=Store())], value=BinOp(left=BinOp(left=BinOp(left=List(elts=[Constant(value=1)], ctx=Load()), op=Mult(), right=Constant(value=10)), op=Add(), right=BinOp(left=List(elts=[Constant(value=2)], ctx=Load()), op=Mult(), right=Constant(value=10))), op=Add(), right=BinOp(left=List(elts=[Constant(value=56.1)], ctx=Load()), op=Mult(), right=Constant(value=10)))), Assign(targets=[Subscript(value=Name(id='none', ctx=Load()), slice=Constant(value=10), ctx=Store())], value=Constant(value=None)), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp'), Constant(value='exog1'), Constant(value='exog2'), Constant(value='exog3'), Constant(value='none')], values=[Name(id='time', ctx=Load()), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='arange', ctx=Load()), args=[Constant(value=100), Constant(value=70), UnaryOp(op=USub(), operand=Constant(value=1))], keywords=[]), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='sin', ctx=Load()), args=[BinOp(left=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='arange', ctx=Load()), args=[Constant(value=30)], keywords=[]), op=Div(), right=Constant(value=10))], keywords=[]), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='exp', ctx=Load()), args=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='arange', ctx=Load()), args=[Constant(value=30)], keywords=[])], keywords=[]), Name(id='none', ctx=Load())])], keywords=[])), Assign(targets=[Name(id='df_exog', ctx=Store())], value=Call(func=Name(id='duplicate_data', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[keyword(arg='segments', value=List(elts=[Constant(value='a'), Constant(value='b')], ctx=Load()))])), Return(value=Tuple(elts=[Name(id='ts', ctx=Load()), Name(id='df_exog', ctx=Load())], ctx=Load()))], decorator_list=[Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load()), args=[], keywords=[])]), FunctionDef(name='test_warnings_statistic_table', args=arguments(posonlyargs=[], args=[arg(arg='columns'), arg(arg='match'), arg(arg='exog_and_target_dfs')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='df', ctx=Store()), Name(id='df_exog', ctx=Store())], ctx=Store())], value=Name(id='exog_and_target_dfs', ctx=Load())), Assign(targets=[Name(id='df_exog', ctx=Store())], value=Subscript(value=Name(id='df_exog', ctx=Load()), slice=ListComp(elt=Name(id='i', ctx=Load()), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Attribute(value=Name(id='df_exog', ctx=Load()), attr='columns', ctx=Load()), ifs=[Compare(left=Subscript(value=Name(id='i', ctx=Load()), slice=Constant(value=1), ctx=Load()), ops=[In()], comparators=[Name(id='columns', ctx=Load())])], is_async=0)]), ctx=Load())), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='warns', ctx=Load()), args=[Name(id='UserWarning', ctx=Load())], keywords=[keyword(arg='match', value=Name(id='match', ctx=Load()))]))], body=[Expr(value=Call(func=Name(id='get_statistics_relevance_table', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load())), keyword(arg='df_exog', value=Name(id='df_exog', ctx=Load()))]))])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='columns,match'), Tuple(elts=[Tuple(elts=[List(elts=[Constant(value='exog1'), Constant(value='exog2'), Constant(value='exog3'), Constant(value='cast')], ctx=Load()), Constant(value='Exogenous data contains columns with category type')], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='exog1'), Constant(value='exog2'), Constant(value='exog3'), Constant(value='none')], ctx=Load()), Constant(value='Exogenous or target data contains None')], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_errors_statistic_table', args=arguments(posonlyargs=[], args=[arg(arg='exog_and_target_dfs')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='df', ctx=Store()), Name(id='df_exog', ctx=Store())], ctx=Store())], value=Name(id='exog_and_target_dfs', ctx=Load())), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='column cannot be cast to float type!'))]))], body=[Expr(value=Call(func=Name(id='get_statistics_relevance_table', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load())), keyword(arg='df_exog', value=Name(id='df_exog', ctx=Load()))]))])], decorator_list=[]), FunctionDef(name='test_work_statistic_table', args=arguments(posonlyargs=[], args=[arg(arg='exog_and_target_dfs')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='df', ctx=Store()), Name(id='df_exog', ctx=Store())], ctx=Store())], value=Name(id='exog_and_target_dfs', ctx=Load())), Assign(targets=[Name(id='df_exog', ctx=Store())], value=Subscript(value=Name(id='df_exog', ctx=Load()), slice=ListComp(elt=Name(id='i', ctx=Load()), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Attribute(value=Name(id='df_exog', ctx=Load()), attr='columns', ctx=Load()), ifs=[Compare(left=Subscript(value=Name(id='i', ctx=Load()), slice=Constant(value=1), ctx=Load()), ops=[NotEq()], comparators=[Constant(value='no_cast')])], is_async=0)]), ctx=Load())), Expr(value=Call(func=Name(id='get_statistics_relevance_table', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load())), keyword(arg='df_exog', value=Name(id='df_exog', ctx=Load()))]))], decorator_list=[]), FunctionDef(name='test_target_none_statistic_table', args=arguments(posonlyargs=[], args=[arg(arg='exog_and_target_dfs_with_none')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='df', ctx=Store()), Name(id='df_exog', ctx=Store())], ctx=Store())], value=Name(id='exog_and_target_dfs_with_none', ctx=Load())), Assign(targets=[Name(id='df_exog', ctx=Store())], value=Subscript(value=Name(id='df_exog', ctx=Load()), slice=ListComp(elt=Name(id='i', ctx=Load()), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Attribute(value=Name(id='df_exog', ctx=Load()), attr='columns', ctx=Load()), ifs=[Compare(left=Subscript(value=Subscript(value=Name(id='i', ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Slice(upper=UnaryOp(op=USub(), operand=Constant(value=1))), ctx=Load()), ops=[Eq()], comparators=[Constant(value='exog')])], is_async=0)]), ctx=Load())), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='warns', ctx=Load()), args=[Name(id='UserWarning', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='Exogenous or target data contains None'))]))], body=[Expr(value=Call(func=Name(id='get_statistics_relevance_table', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load())), keyword(arg='df_exog', value=Name(id='df_exog', ctx=Load()))]))])], decorator_list=[]), FunctionDef(name='test_target_none_model_table', args=arguments(posonlyargs=[], args=[arg(arg='exog_and_target_dfs_with_none')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='df', ctx=Store()), Name(id='df_exog', ctx=Store())], ctx=Store())], value=Name(id='exog_and_target_dfs_with_none', ctx=Load())), Assign(targets=[Name(id='df_exog', ctx=Store())], value=Subscript(value=Name(id='df_exog', ctx=Load()), slice=ListComp(elt=Name(id='i', ctx=Load()), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Attribute(value=Name(id='df_exog', ctx=Load()), attr='columns', ctx=Load()), ifs=[Compare(left=Subscript(value=Subscript(value=Name(id='i', ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Slice(upper=UnaryOp(op=USub(), operand=Constant(value=1))), ctx=Load()), ops=[Eq()], comparators=[Constant(value='exog')])], is_async=0)]), ctx=Load())), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='warns', ctx=Load()), args=[Name(id='UserWarning', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='Exogenous or target data contains None'))]))], body=[Expr(value=Call(func=Name(id='get_model_relevance_table', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load())), keyword(arg='df_exog', value=Name(id='df_exog', ctx=Load())), keyword(arg='model', value=Call(func=Name(id='DecisionTreeRegressor', ctx=Load()), args=[], keywords=[]))]))])], decorator_list=[]), FunctionDef(name='test_exog_none_model_table', args=arguments(posonlyargs=[], args=[arg(arg='exog_and_target_dfs')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='df', ctx=Store()), Name(id='df_exog', ctx=Store())], ctx=Store())], value=Name(id='exog_and_target_dfs', ctx=Load())), Assign(targets=[Name(id='df_exog', ctx=Store())], value=Subscript(value=Name(id='df_exog', ctx=Load()), slice=ListComp(elt=Name(id='i', ctx=Load()), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Attribute(value=Name(id='df_exog', ctx=Load()), attr='columns', ctx=Load()), ifs=[Compare(left=Subscript(value=Name(id='i', ctx=Load()), slice=Constant(value=1), ctx=Load()), ops=[In()], comparators=[List(elts=[Constant(value='exog1'), Constant(value='exog2'), Constant(value='exog3'), Constant(value='none')], ctx=Load())])], is_async=0)]), ctx=Load())), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='warns', ctx=Load()), args=[Name(id='UserWarning', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='Exogenous or target data contains None'))]))], body=[Expr(value=Call(func=Name(id='get_model_relevance_table', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load())), keyword(arg='df_exog', value=Name(id='df_exog', ctx=Load())), keyword(arg='model', value=Call(func=Name(id='DecisionTreeRegressor', ctx=Load()), args=[], keywords=[]))]))])], decorator_list=[]), FunctionDef(name='test_exog_and_target_none_statistic_table', args=arguments(posonlyargs=[], args=[arg(arg='exog_and_target_dfs_with_none')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='df', ctx=Store()), Name(id='df_exog', ctx=Store())], ctx=Store())], value=Name(id='exog_and_target_dfs_with_none', ctx=Load())), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='warns', ctx=Load()), args=[Name(id='UserWarning', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='Exogenous or target data contains None'))]))], body=[Expr(value=Call(func=Name(id='get_statistics_relevance_table', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load())), keyword(arg='df_exog', value=Name(id='df_exog', ctx=Load()))]))])], decorator_list=[]), FunctionDef(name='test_exog_and_target_none_model_table', args=arguments(posonlyargs=[], args=[arg(arg='exog_and_target_dfs_with_none')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='df', ctx=Store()), Name(id='df_exog', ctx=Store())], ctx=Store())], value=Name(id='exog_and_target_dfs_with_none', ctx=Load())), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='warns', ctx=Load()), args=[Name(id='UserWarning', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='Exogenous or target data contains None'))]))], body=[Expr(value=Call(func=Name(id='get_model_relevance_table', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load())), keyword(arg='df_exog', value=Name(id='df_exog', ctx=Load())), keyword(arg='model', value=Call(func=Name(id='DecisionTreeRegressor', ctx=Load()), args=[], keywords=[]))]))])], decorator_list=[])], type_ignores=[])