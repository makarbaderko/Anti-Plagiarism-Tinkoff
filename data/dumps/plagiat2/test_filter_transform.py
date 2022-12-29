Module(body=[Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), Import(names=[alias(name='pytest')]), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.transforms.feature_selection', names=[alias(name='FilterFeaturesTransform')], level=0), FunctionDef(name='test_exclude_filter', args=arguments(posonlyargs=[], args=[arg(arg='ts_with_featuresO'), arg(arg='exclude'), arg(arg='expected_columns')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='original_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='FilterFeaturesTransform', ctx=Load()), args=[], keywords=[keyword(arg='exclude', value=Name(id='exclude', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='transform', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='df_transformed', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='got_columns', ctx=Store())], value=Call(func=Name(id='s', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='df_transformed', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[])], keywords=[])), Assert(test=Compare(left=Name(id='got_columns', ctx=Load()), ops=[Eq()], comparators=[Call(func=Name(id='s', ctx=Load()), args=[Name(id='expected_columns', ctx=Load())], keywords=[])])), For(target=Name(id='column', ctx=Store()), iter=Name(id='got_columns', ctx=Load()), body=[Assert(test=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='all', ctx=Load()), args=[Compare(left=Subscript(value=Attribute(value=Name(id='df_transformed', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), ops=[Eq()], comparators=[Subscript(value=Attribute(value=Name(id='original_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())])], keywords=[]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='exclude, expected_columns'), List(elts=[Tuple(elts=[List(elts=[], ctx=Load()), List(elts=[Constant(value='target'), Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='target')], ctx=Load()), List(elts=[Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load()), List(elts=[Constant(value='target')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='target'), Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load()), List(elts=[], ctx=Load())], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_set_onl', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Name(id='FilterFeaturesTransform', ctx=Load()), args=[], keywords=[keyword(arg='exclude', value=List(elts=[Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load()))]))], decorator_list=[]), FunctionDef(name='test_t', args=arguments(posonlyargs=[], args=[arg(arg='ts_with_featuresO'), arg(arg='columns'), arg(arg='saved_columns'), arg(arg='return_features')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='original_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='FilterFeaturesTransform', ctx=Load()), args=[], keywords=[keyword(arg='include', value=Name(id='columns', ctx=Load())), keyword(arg='return_features', value=Name(id='return_features', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='transform', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='df_transformed', ctx=Store())], value=Attribute(value=Name(id='transform', ctx=Load()), attr='_df_removed', ctx=Load())), If(test=Name(id='return_features', ctx=Load()), body=[Assign(targets=[Name(id='got_columns', ctx=Store())], value=Call(func=Name(id='s', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='df_transformed', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[])], keywords=[])), Assert(test=Compare(left=Name(id='got_columns', ctx=Load()), ops=[Eq()], comparators=[Call(func=Name(id='s', ctx=Load()), args=[Name(id='saved_columns', ctx=Load())], keywords=[])])), For(target=Name(id='column', ctx=Store()), iter=Name(id='got_columns', ctx=Load()), body=[Assert(test=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='all', ctx=Load()), args=[Compare(left=Subscript(value=Attribute(value=Name(id='df_transformed', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), ops=[Eq()], comparators=[Subscript(value=Attribute(value=Name(id='original_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())])], keywords=[]))], orelse=[])], orelse=[Assert(test=Compare(left=Name(id='df_transformed', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]))])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='return_features'), List(elts=[Constant(value=True), Constant(value=False)], ctx=Load())], keywords=[]), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='columns, saved_columns'), List(elts=[Tuple(elts=[List(elts=[], ctx=Load()), List(elts=[Constant(value='target'), Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='target')], ctx=Load()), List(elts=[Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load()), List(elts=[Constant(value='target')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='target'), Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load()), List(elts=[], ctx=Load())], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_set_include_and_exclude', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ſT˩ˀĠeRsϓt tʡhaɍt ȃtranMsτfo±ήϱòqͫrm ȥϊŷis̶̉Üˡ noĂt\xad +cr»e\x9eɷǢaϧ˩\x9cũtʿedɇǢ witǄ\x9bhƚ inΦcêȚlʉuìǱde\x93 ʜˮand eǮžxcĐlĹudę̯.ɜ')), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='There should be exactly one option set: include or exclude'))]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Name(id='FilterFeaturesTransform', ctx=Load()), args=[], keywords=[keyword(arg='include', value=List(elts=[Constant(value='exog_1')], ctx=Load())), keyword(arg='exclude', value=List(elts=[Constant(value='exog_2')], ctx=Load()))]))])], decorator_list=[]), FunctionDef(name='test_set_none', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='There should be exactly one option set: include or exclude'))]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Name(id='FilterFeaturesTransform', ctx=Load()), args=[], keywords=[]))])], decorator_list=[]), FunctionDef(name='test_include_filter', args=arguments(posonlyargs=[], args=[arg(arg='ts_with_featuresO'), arg(arg='INCLUDE')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Test that transform remains only features in include.')), Assign(targets=[Name(id='original_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='FilterFeaturesTransform', ctx=Load()), args=[], keywords=[keyword(arg='include', value=Name(id='INCLUDE', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='transform', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='df_transformed', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='expected_columns', ctx=Store())], value=Call(func=Name(id='s', ctx=Load()), args=[Name(id='INCLUDE', ctx=Load())], keywords=[])), Assign(targets=[Name(id='got_columns', ctx=Store())], value=Call(func=Name(id='s', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='df_transformed', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[])], keywords=[])), Assert(test=Compare(left=Name(id='got_columns', ctx=Load()), ops=[Eq()], comparators=[Name(id='expected_columns', ctx=Load())])), For(target=Name(id='column', ctx=Store()), iter=Name(id='got_columns', ctx=Load()), body=[Assert(test=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='all', ctx=Load()), args=[Compare(left=Subscript(value=Attribute(value=Name(id='df_transformed', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), ops=[Eq()], comparators=[Subscript(value=Attribute(value=Name(id='original_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())])], keywords=[]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='include'), List(elts=[List(elts=[], ctx=Load()), List(elts=[Constant(value='target')], ctx=Load()), List(elts=[Constant(value='exog_1')], ctx=Load()), List(elts=[Constant(value='exog_1'), Constant(value='exog_2'), Constant(value='target')], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_ex_clude_filter_wrong_column', args=arguments(posonlyargs=[], args=[arg(arg='ts_with_featuresO')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Test˃ that transform raises error with non-existeʙnt column in exclłude.')), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='FilterFeaturesTransform', ctx=Load()), args=[], keywords=[keyword(arg='exclude', value=List(elts=[Constant(value='non-existent-column')], ctx=Load()))])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='Features {.*} are not present in the dataset'))]))], body=[Expr(value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='transform', ctx=Load())], ctx=Load())], keywords=[]))])], decorator_list=[]), FunctionDef(name='test_include_filter_wrong_column', args=arguments(posonlyargs=[], args=[arg(arg='ts_with_featuresO')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Tψeθsϵt thaėtʰ ƴtransfčâorƑmČ raises error with nǮon-ŧȯexistent̕ colūumn inǉϋ¦ ʢƞinclªud\x88eș¸.')), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='FilterFeaturesTransform', ctx=Load()), args=[], keywords=[keyword(arg='include', value=List(elts=[Constant(value='non-existent-column')], ctx=Load()))])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='Features {.*} are not present in the dataset'))]))], body=[Expr(value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='transform', ctx=Load())], ctx=Load())], keywords=[]))])], decorator_list=[]), FunctionDef(name='ts_with_featuresO', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='timest', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[keyword(arg='periods', value=Constant(value=100)), keyword(arg='freq', value=Constant(value='D'))])), Assign(targets=[Name(id='df_1_', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp'), Constant(value='segment'), Constant(value='target')], values=[Name(id='timest', ctx=Load()), Constant(value='segment_1'), Constant(value=1)])], keywords=[])), Assign(targets=[Name(id='df_2', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp'), Constant(value='segment'), Constant(value='target')], values=[Name(id='timest', ctx=Load()), Constant(value='segment_2'), Constant(value=2)])], keywords=[])), Assign(targets=[Name(id='DF', ctx=Store())], value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[List(elts=[Name(id='df_1_', ctx=Load()), Name(id='df_2', ctx=Load())], ctx=Load())], keywords=[keyword(arg='ignore_index', value=Constant(value=False))])], keywords=[])), Assign(targets=[Name(id='df_exog_1', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp'), Constant(value='segment'), Constant(value='exog_1'), Constant(value='exog_2')], values=[Name(id='timest', ctx=Load()), Constant(value='segment_1'), Constant(value=1), Constant(value=2)])], keywords=[])), Assign(targets=[Name(id='df_exo_g_2', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp'), Constant(value='segment'), Constant(value='exog_1'), Constant(value='exog_2')], values=[Name(id='timest', ctx=Load()), Constant(value='segment_2'), Constant(value=3), Constant(value=4)])], keywords=[])), Assign(targets=[Name(id='df_exog', ctx=Store())], value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[List(elts=[Name(id='df_exog_1', ctx=Load()), Name(id='df_exo_g_2', ctx=Load())], ctx=Load())], keywords=[keyword(arg='ignore_index', value=Constant(value=False))])], keywords=[])), Return(value=Call(func=Name(id='TSDataset', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='DF', ctx=Load())), keyword(arg='df_exog', value=Name(id='df_exog', ctx=Load())), keyword(arg='freq', value=Constant(value='D'))]))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='test_transform_exclude_save_columns', args=arguments(posonlyargs=[], args=[arg(arg='ts_with_featuresO'), arg(arg='columns'), arg(arg='saved_columns'), arg(arg='return_features')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='  ̘ʫŨ     1 Ð \x7f     ')), Assign(targets=[Name(id='original_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='FilterFeaturesTransform', ctx=Load()), args=[], keywords=[keyword(arg='exclude', value=Name(id='columns', ctx=Load())), keyword(arg='return_features', value=Name(id='return_features', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='transform', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='df_transformed', ctx=Store())], value=Attribute(value=Name(id='transform', ctx=Load()), attr='_df_removed', ctx=Load())), If(test=Name(id='return_features', ctx=Load()), body=[Assign(targets=[Name(id='got_columns', ctx=Store())], value=Call(func=Name(id='s', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='df_transformed', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[])], keywords=[])), Assert(test=Compare(left=Name(id='got_columns', ctx=Load()), ops=[Eq()], comparators=[Call(func=Name(id='s', ctx=Load()), args=[Name(id='saved_columns', ctx=Load())], keywords=[])])), For(target=Name(id='column', ctx=Store()), iter=Name(id='got_columns', ctx=Load()), body=[Assert(test=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='all', ctx=Load()), args=[Compare(left=Subscript(value=Attribute(value=Name(id='df_transformed', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), ops=[Eq()], comparators=[Subscript(value=Attribute(value=Name(id='original_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())])], keywords=[]))], orelse=[])], orelse=[Assert(test=Compare(left=Name(id='df_transformed', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]))])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='return_features'), List(elts=[Constant(value=True), Constant(value=False)], ctx=Load())], keywords=[]), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='columns, saved_columns'), List(elts=[Tuple(elts=[List(elts=[], ctx=Load()), List(elts=[], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='target')], ctx=Load()), List(elts=[Constant(value='target')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load()), List(elts=[Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='target'), Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load()), List(elts=[Constant(value='target'), Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load())], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_set_only_in', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Name(id='FilterFeaturesTransform', ctx=Load()), args=[], keywords=[keyword(arg='include', value=List(elts=[Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load()))]))], decorator_list=[]), FunctionDef(name='test_inverse_transform_back_excluded_columns', args=arguments(posonlyargs=[], args=[arg(arg='ts_with_featuresO'), arg(arg='columns'), arg(arg='return_features'), arg(arg='expected_columns')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' ʔ    ɜ Ɲ  ')), Assign(targets=[Name(id='original_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='FilterFeaturesTransform', ctx=Load()), args=[], keywords=[keyword(arg='exclude', value=Name(id='columns', ctx=Load())), keyword(arg='return_features', value=Name(id='return_features', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='transform', ctx=Load())], ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='columns_inverseddXgKO', ctx=Store())], value=Call(func=Name(id='s', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[])], keywords=[])), Assert(test=Compare(left=Name(id='columns_inverseddXgKO', ctx=Load()), ops=[Eq()], comparators=[Call(func=Name(id='s', ctx=Load()), args=[Name(id='expected_columns', ctx=Load())], keywords=[])])), For(target=Name(id='column', ctx=Store()), iter=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='columns', ctx=Load()), body=[Assert(test=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='all', ctx=Load()), args=[Compare(left=Subscript(value=Name(id='ts_with_featuresO', ctx=Load()), slice=Tuple(elts=[Slice(), Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load()), ops=[Eq()], comparators=[Subscript(value=Attribute(value=Name(id='original_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())])], keywords=[]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='columns, return_features, expected_columns'), List(elts=[Tuple(elts=[List(elts=[], ctx=Load()), Constant(value=True), List(elts=[Constant(value='exog_1'), Constant(value='target'), Constant(value='exog_2')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[], ctx=Load()), Constant(value=False), List(elts=[Constant(value='target'), Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='target')], ctx=Load()), Constant(value=True), List(elts=[Constant(value='exog_1'), Constant(value='target'), Constant(value='exog_2')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='target')], ctx=Load()), Constant(value=False), List(elts=[Constant(value='exog_2'), Constant(value='exog_1')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load()), Constant(value=True), List(elts=[Constant(value='exog_1'), Constant(value='target'), Constant(value='exog_2')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load()), Constant(value=False), List(elts=[Constant(value='target')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='target'), Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load()), Constant(value=True), List(elts=[Constant(value='exog_1'), Constant(value='target'), Constant(value='exog_2')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='target'), Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load()), Constant(value=False), List(elts=[], ctx=Load())], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_inverse_transform_back_inc', args=arguments(posonlyargs=[], args=[arg(arg='ts_with_featuresO'), arg(arg='columns'), arg(arg='return_features'), arg(arg='expected_columns')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='   Ļ  ')), Assign(targets=[Name(id='original_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='FilterFeaturesTransform', ctx=Load()), args=[], keywords=[keyword(arg='include', value=Name(id='columns', ctx=Load())), keyword(arg='return_features', value=Name(id='return_features', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='transform', ctx=Load())], ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='columns_inverseddXgKO', ctx=Store())], value=Call(func=Name(id='s', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[])], keywords=[])), Assert(test=Compare(left=Name(id='columns_inverseddXgKO', ctx=Load()), ops=[Eq()], comparators=[Call(func=Name(id='s', ctx=Load()), args=[Name(id='expected_columns', ctx=Load())], keywords=[])])), For(target=Name(id='column', ctx=Store()), iter=Attribute(value=Name(id='ts_with_featuresO', ctx=Load()), attr='columns', ctx=Load()), body=[Assert(test=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='all', ctx=Load()), args=[Compare(left=Subscript(value=Name(id='ts_with_featuresO', ctx=Load()), slice=Tuple(elts=[Slice(), Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load()), ops=[Eq()], comparators=[Subscript(value=Attribute(value=Name(id='original_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())])], keywords=[]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='columns, return_features, expected_columns'), List(elts=[Tuple(elts=[List(elts=[], ctx=Load()), Constant(value=True), List(elts=[Constant(value='exog_1'), Constant(value='target'), Constant(value='exog_2')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[], ctx=Load()), Constant(value=False), List(elts=[], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='target')], ctx=Load()), Constant(value=True), List(elts=[Constant(value='exog_1'), Constant(value='target'), Constant(value='exog_2')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='target')], ctx=Load()), Constant(value=False), List(elts=[Constant(value='target')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load()), Constant(value=True), List(elts=[Constant(value='exog_1'), Constant(value='target'), Constant(value='exog_2')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load()), Constant(value=False), List(elts=[Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='target'), Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load()), Constant(value=True), List(elts=[Constant(value='exog_1'), Constant(value='target'), Constant(value='exog_2')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='target'), Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load()), Constant(value=False), List(elts=[Constant(value='exog_1'), Constant(value='target'), Constant(value='exog_2')], ctx=Load())], ctx=Load())], ctx=Load())], keywords=[])])], type_ignores=[])