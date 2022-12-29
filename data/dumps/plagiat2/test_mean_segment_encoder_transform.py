Module(body=[Import(names=[alias(name='numpy', asname='np')]), ImportFrom(module='etna.models', names=[alias(name='LinearMultiSegmentModel')], level=0), Import(names=[alias(name='pytest')]), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='R2')], level=0), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='etna.transforms', names=[alias(name='MeanSegmentEncoderTransform')], level=0), FunctionDef(name='test_mean_segment_encod', args=arguments(posonlyargs=[], args=[arg(arg='simple_df'), arg(arg='EXPECTED_GLOBAL_MEANS')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='encoder', ctx=Store())], value=Call(func=Name(id='MeanSegmentEncoderTransform', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='encoder', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='simple_df', ctx=Load())], keywords=[])), Assert(test=Call(func=Attribute(value=Compare(left=Attribute(value=Name(id='encoder', ctx=Load()), attr='global_means', ctx=Load()), ops=[Eq()], comparators=[Name(id='EXPECTED_GLOBAL_MEANS', ctx=Load())]), attr='all', ctx=Load()), args=[], keywords=[]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='expected_global_means'), List(elts=[List(elts=[Constant(value=3), Constant(value=30)], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_mean_segme', args=arguments(posonlyargs=[], args=[arg(arg='simple_df'), arg(arg='transformed_simple_df')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' ¢Ǥ  ǰȠϲ     Ȟϝ Ώʸ')), Assign(targets=[Name(id='encoder', ctx=Store())], value=Call(func=Name(id='MeanSegmentEncoderTransform', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transformed_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='encoder', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Name(id='simple_df', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='pd', ctx=Load()), attr='testing', ctx=Load()), attr='assert_frame_equal', ctx=Load()), args=[Name(id='transformed_df', ctx=Load()), Name(id='transformed_simple_df', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='test_mean_segment_encoder_forecast', args=arguments(posonlyargs=[], args=[arg(arg='almost_constant_ts')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='horizona', ctx=Store())], value=Constant(value=5)), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='LinearMultiSegmentModel', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='encoder', ctx=Store())], value=Call(func=Name(id='MeanSegmentEncoderTransform', ctx=Load()), args=[], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='_train', ctx=Store()), Name(id='test', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='almost_constant_ts', ctx=Load()), attr='train_test_split', ctx=Load()), args=[], keywords=[keyword(arg='test_size', value=Name(id='horizona', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='_train', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='encoder', ctx=Load())], ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='_train', ctx=Load())], keywords=[])), Assign(targets=[Name(id='future', ctx=Store())], value=Call(func=Attribute(value=Name(id='_train', ctx=Load()), attr='make_future', ctx=Load()), args=[Name(id='horizona', ctx=Load())], keywords=[])), Assign(targets=[Name(id='pred_mean_segment_encoding', ctx=Store())], value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='forecast', ctx=Load()), args=[Name(id='future', ctx=Load())], keywords=[])), Assign(targets=[Name(id='me', ctx=Store())], value=Call(func=Name(id='R2', ctx=Load()), args=[], keywords=[keyword(arg='mode', value=Constant(value='macro'))])), Assert(test=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='allclose', ctx=Load()), args=[Call(func=Name(id='me', ctx=Load()), args=[Name(id='pred_mean_segment_encoding', ctx=Load()), Name(id='test', ctx=Load())], keywords=[]), Constant(value=0)], keywords=[]))], decorator_list=[]), FunctionDef(name='almost_constant_ts', args=arguments(posonlyargs=[], args=[arg(arg='random_seed')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='df_1', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), attr='from_dict', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp')], values=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[Constant(value='2021-06-01'), Constant(value='2021-07-01')], keywords=[keyword(arg='freq', value=Constant(value='D'))])])], keywords=[])), Assign(targets=[Name(id='df_2', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), attr='from_dict', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp')], values=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[Constant(value='2021-06-01'), Constant(value='2021-07-01')], keywords=[keyword(arg='freq', value=Constant(value='D'))])])], keywords=[])), Assign(targets=[Subscript(value=Name(id='df_1', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=Constant(value='Moscow')), Assign(targets=[Subscript(value=Name(id='df_1', ctx=Load()), slice=Constant(value='target'), ctx=Store())], value=BinOp(left=Constant(value=1), op=Add(), right=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='normal', ctx=Load()), args=[Constant(value=0), Constant(value=0.1)], keywords=[keyword(arg='size', value=Call(func=Name(id='len', ctx=Load()), args=[Name(id='df_1', ctx=Load())], keywords=[]))]))), Assign(targets=[Subscript(value=Name(id='df_2', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=Constant(value='Omsk')), Assign(targets=[Subscript(value=Name(id='df_2', ctx=Load()), slice=Constant(value='target'), ctx=Store())], value=BinOp(left=Constant(value=10), op=Add(), right=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='normal', ctx=Load()), args=[Constant(value=0), Constant(value=0.1)], keywords=[keyword(arg='size', value=Call(func=Name(id='len', ctx=Load()), args=[Name(id='df_1', ctx=Load())], keywords=[]))]))), Assign(targets=[Name(id='classic_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[List(elts=[Name(id='df_1', ctx=Load()), Name(id='df_2', ctx=Load())], ctx=Load())], keywords=[keyword(arg='ignore_index', value=Constant(value=True))])), Assign(targets=[Name(id='t', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Name(id='classic_df', ctx=Load())], keywords=[])), keyword(arg='freq', value=Constant(value='D'))])), Return(value=Name(id='t', ctx=Load()))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='test_fit_transfor', args=arguments(posonlyargs=[], args=[arg(arg='ts_diff_endings')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ϊ  Ƕq ʾ   ')), Assign(targets=[Name(id='encoder', ctx=Store())], value=Call(func=Name(id='MeanSegmentEncoderTransform', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='ts_diff_endings', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='encoder', ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[])], type_ignores=[])