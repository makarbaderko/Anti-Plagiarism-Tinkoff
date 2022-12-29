Module(body=[Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pytest')]), ImportFrom(module='sklearn.linear_model', names=[alias(name='LogisticRegression')], level=0), ImportFrom(module='etna.experimental.classification.feature_extraction', names=[alias(name='WEASELFeatureExtractor')], level=0), ImportFrom(module='etna.experimental.classification.feature_extraction.weasel', names=[alias(name='CustomWEASEL')], level=0), FunctionDef(name='many_time_series_big', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='           ')), Assign(targets=[Name(id='x', ctx=Store())], value=ListComp(elt=Subscript(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='randint', ctx=Load()), args=[Constant(value=0), Constant(value=1000)], keywords=[keyword(arg='size', value=Constant(value=100))]), slice=Slice(upper=Name(id='i', ctx=Load())), ctx=Load()), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Constant(value=50), Constant(value=80)], keywords=[]), ifs=[], is_async=0)])), Assign(targets=[Name(id='Y', ctx=Store())], value=ListComp(elt=Subscript(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='randint', ctx=Load()), args=[Constant(value=0), Constant(value=2)], keywords=[keyword(arg='size', value=Constant(value=1))]), slice=Constant(value=0), ctx=Load()), generators=[comprehension(target=Name(id='_', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Constant(value=50), Constant(value=80)], keywords=[]), ifs=[], is_async=0)])), Return(value=Tuple(elts=[Name(id='x', ctx=Load()), Name(id='Y', ctx=Load())], ctx=Load()))], decorator_list=[Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load()), args=[], keywords=[])]), FunctionDef(name='many_time_series_windowed_3_1', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='   Ę ªƚßɀ ʬï   ˪ Ə   ')), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='array', ctx=Load()), args=[List(elts=[List(elts=[Constant(value=1.0), Constant(value=2.0), Constant(value=3.0)], ctx=Load()), List(elts=[Constant(value=2.0), Constant(value=3.0), Constant(value=4.0)], ctx=Load()), List(elts=[Constant(value=4.0), Constant(value=4.0), Constant(value=4.0)], ctx=Load()), List(elts=[Constant(value=5.0), Constant(value=5.0), Constant(value=5.0)], ctx=Load()), List(elts=[Constant(value=5.0), Constant(value=5.0), Constant(value=6.0)], ctx=Load()), List(elts=[Constant(value=5.0), Constant(value=6.0), Constant(value=7.0)], ctx=Load()), List(elts=[Constant(value=6.0), Constant(value=7.0), Constant(value=8.0)], ctx=Load()), List(elts=[Constant(value=7.0), Constant(value=8.0), Constant(value=9.0)], ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='Y', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='array', ctx=Load()), args=[List(elts=[Constant(value=1), Constant(value=1), Constant(value=0), Constant(value=1), Constant(value=1), Constant(value=1), Constant(value=1), Constant(value=1)], ctx=Load())], keywords=[])), Assign(targets=[Name(id='cum_sum', ctx=Store())], value=List(elts=[Constant(value=0), Constant(value=2), Constant(value=3), Constant(value=8)], ctx=Load())), Return(value=Tuple(elts=[Name(id='x', ctx=Load()), Name(id='Y', ctx=Load()), Name(id='cum_sum', ctx=Load())], ctx=Load()))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())]), FunctionDef(name='many_time_series_windowed_3_2', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' !  ̫      Ñăȿ Ȧǐ ɳ    ˾  ')), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='array', ctx=Load()), args=[List(elts=[List(elts=[Constant(value=2.0), Constant(value=3.0), Constant(value=4.0)], ctx=Load()), List(elts=[Constant(value=4.0), Constant(value=4.0), Constant(value=4.0)], ctx=Load()), List(elts=[Constant(value=5.0), Constant(value=5.0), Constant(value=5.0)], ctx=Load()), List(elts=[Constant(value=5.0), Constant(value=6.0), Constant(value=7.0)], ctx=Load()), List(elts=[Constant(value=7.0), Constant(value=8.0), Constant(value=9.0)], ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='Y', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='array', ctx=Load()), args=[List(elts=[Constant(value=1), Constant(value=0), Constant(value=1), Constant(value=1), Constant(value=1)], ctx=Load())], keywords=[])), Assign(targets=[Name(id='cum_sum', ctx=Store())], value=List(elts=[Constant(value=0), Constant(value=1), Constant(value=2), Constant(value=5)], ctx=Load())), Return(value=Tuple(elts=[Name(id='x', ctx=Load()), Name(id='Y', ctx=Load()), Name(id='cum_sum', ctx=Load())], ctx=Load()))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())]), FunctionDef(name='test_windowed_view', args=arguments(posonlyargs=[], args=[arg(arg='many_time_series'), arg(arg='window_size'), arg(arg='window_step'), arg(arg='expected'), arg(arg='request')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='x', ctx=Store()), Name(id='Y', ctx=Store())], ctx=Store())], value=Name(id='many_time_series', ctx=Load())), Assign(targets=[Tuple(elts=[Name(id='x_windowed_expected', ctx=Store()), Name(id='y_windowed_expected', ctx=Store()), Name(id='n_windows_per_sample_cum_expected', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='request', ctx=Load()), attr='getfixturevalue', ctx=Load()), args=[Name(id='expected', ctx=Load())], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='x_windowed', ctx=Store()), Name(id='y_windowed', ctx=Store()), Name(id='n_windows_per_sample_cum', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='CustomWEASEL', ctx=Load()), attr='_windowed_view', ctx=Load()), args=[], keywords=[keyword(arg='x', value=Name(id='x', ctx=Load())), keyword(arg='y', value=Name(id='Y', ctx=Load())), keyword(arg='window_size', value=Name(id='window_size', ctx=Load())), keyword(arg='window_step', value=Name(id='window_step', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='testing', ctx=Load()), attr='assert_array_equal', ctx=Load()), args=[Name(id='x_windowed', ctx=Load()), Name(id='x_windowed_expected', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='testing', ctx=Load()), attr='assert_array_equal', ctx=Load()), args=[Name(id='y_windowed', ctx=Load()), Name(id='y_windowed_expected', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='testing', ctx=Load()), attr='assert_array_equal', ctx=Load()), args=[Name(id='n_windows_per_sample_cum', ctx=Load()), Name(id='n_windows_per_sample_cum_expected', ctx=Load())], keywords=[]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='window_size, window_step, expected'), List(elts=[Tuple(elts=[Constant(value=3), Constant(value=1), Constant(value='many_time_series_windowed_3_1')], ctx=Load()), Tuple(elts=[Constant(value=3), Constant(value=2), Constant(value='many_time_series_windowed_3_2')], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_preprocessor_and_classifier', args=arguments(posonlyargs=[], args=[arg(arg='many_time_series_big')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='x', ctx=Store()), Name(id='Y', ctx=Store())], ctx=Store())], value=Name(id='many_time_series_big', ctx=Load())), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='LogisticRegression', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='feature_extractor', ctx=Store())], value=Call(func=Name(id='WEASELFeatureExtractor', ctx=Load()), args=[], keywords=[keyword(arg='padding_value', value=Constant(value=0)), keyword(arg='window_sizes', value=List(elts=[Constant(value=10), Constant(value=15)], ctx=Load()))])), Assign(targets=[Name(id='x_tr', ctx=Store())], value=Call(func=Attribute(value=Name(id='feature_extractor', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Name(id='x', ctx=Load()), Name(id='Y', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='x_tr', ctx=Load()), Name(id='Y', ctx=Load())], keywords=[]))], decorator_list=[])], type_ignores=[])