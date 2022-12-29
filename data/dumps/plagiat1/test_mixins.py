Module(body=[ImportFrom(module='unittest.mock', names=[alias(name='MagicMock')], level=0), Import(names=[alias(name='pandas', asname='pd')]), Import(names=[alias(name='pytest')]), ImportFrom(module='etna.models.base', names=[alias(name='NonPredictionIntervalContextIgnorantAbstractModel')], level=0), ImportFrom(module='etna.models.base', names=[alias(name='NonPredictionIntervalContextRequiredAbstractModel')], level=0), ImportFrom(module='etna.models.base', names=[alias(name='PredictionIntervalContextIgnorantAbstractModel')], level=0), ImportFrom(module='etna.models.base', names=[alias(name='PredictionIntervalContextRequiredAbstractModel')], level=0), ImportFrom(module='etna.pipeline.mixins', names=[alias(name='ModelPipelinePredictMixin')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='DateFlagsTransform')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='FilterFeaturesTransform')], level=0), FunctionDef(name='make_mixin', args=arguments(posonlyargs=[], args=[arg(arg='model'), arg(arg='transforms'), arg(arg='mock_recreate_ts'), arg(arg='mock_determine_prediction_size')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None), Tuple(elts=[], ctx=Load()), Constant(value=True), Constant(value=True)]), body=[If(test=Compare(left=Name(id='model', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[keyword(arg='spec', value=Name(id='NonPredictionIntervalContextIgnorantAbstractModel', ctx=Load()))]))], orelse=[]), Assign(targets=[Name(id='mixin', ctx=Store())], value=Call(func=Name(id='ModelPipelinePredictMixin', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='mixin', ctx=Load()), attr='transforms', ctx=Store())], value=Name(id='transforms', ctx=Load())), Assign(targets=[Attribute(value=Name(id='mixin', ctx=Load()), attr='model', ctx=Store())], value=Name(id='model', ctx=Load())), If(test=Name(id='mock_recreate_ts', ctx=Load()), body=[Assign(targets=[Attribute(value=Name(id='mixin', ctx=Load()), attr='_create_ts', ctx=Store())], value=Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[]))], orelse=[]), If(test=Name(id='mock_determine_prediction_size', ctx=Load()), body=[Assign(targets=[Attribute(value=Name(id='mixin', ctx=Load()), attr='_determine_prediction_size', ctx=Store())], value=Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[]))], orelse=[]), Return(value=Name(id='mixin', ctx=Load()))], decorator_list=[]), FunctionDef(name='test_create_ts', args=arguments(posonlyargs=[], args=[arg(arg='context_size'), arg(arg='start_timestamp'), arg(arg='end_timestamp'), arg(arg='transforms'), arg(arg='example_reg_tsds')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='ts', ctx=Store())], value=Name(id='example_reg_tsds', ctx=Load())), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='model', ctx=Load()), attr='context_size', ctx=Store())], value=Name(id='context_size', ctx=Load())), Assign(targets=[Name(id='mixin', ctx=Store())], value=Call(func=Name(id='make_mixin', ctx=Load()), args=[], keywords=[keyword(arg='transforms', value=Name(id='transforms', ctx=Load())), keyword(arg='model', value=Name(id='model', ctx=Load())), keyword(arg='mock_recreate_ts', value=Constant(value=False))])), Expr(value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Name(id='transforms', ctx=Load())], keywords=[])), Assign(targets=[Name(id='cr', ctx=Store())], value=Call(func=Attribute(value=Name(id='mixin', ctx=Load()), attr='_create_ts', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='start_timestamp', value=Name(id='start_timestamp', ctx=Load())), keyword(arg='end_timestamp', value=Name(id='end_timestamp', ctx=Load()))])), Assign(targets=[Name(id='expected_start_timestamp', ctx=Store())], value=Call(func=Name(id='max', ctx=Load()), args=[Subscript(value=Attribute(value=Name(id='example_reg_tsds', ctx=Load()), attr='index', ctx=Load()), slice=Constant(value=0), ctx=Load()), BinOp(left=Name(id='start_timestamp', ctx=Load()), op=Sub(), right=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timedelta', ctx=Load()), args=[], keywords=[keyword(arg='days', value=Attribute(value=Name(id='model', ctx=Load()), attr='context_size', ctx=Load()))]))], keywords=[])), Assert(test=Compare(left=Subscript(value=Attribute(value=Name(id='cr', ctx=Load()), attr='index', ctx=Load()), slice=Constant(value=0), ctx=Load()), ops=[Eq()], comparators=[Name(id='expected_start_timestamp', ctx=Load())])), Assert(test=Compare(left=Subscript(value=Attribute(value=Name(id='cr', ctx=Load()), attr='index', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=1)), ctx=Load()), ops=[Eq()], comparators=[Name(id='end_timestamp', ctx=Load())])), Assert(test=Compare(left=Attribute(value=Name(id='cr', ctx=Load()), attr='regressors', ctx=Load()), ops=[Eq()], comparators=[Attribute(value=Name(id='ts', ctx=Load()), attr='regressors', ctx=Load())])), Assign(targets=[Name(id='expected_df', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='ts', ctx=Load()), attr='df', ctx=Load()), slice=Slice(lower=Name(id='expected_start_timestamp', ctx=Load()), upper=Name(id='end_timestamp', ctx=Load())), ctx=Load())), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='pd', ctx=Load()), attr='testing', ctx=Load()), attr='assert_frame_equal', ctx=Load()), args=[Attribute(value=Name(id='cr', ctx=Load()), attr='df', ctx=Load()), Name(id='expected_df', ctx=Load())], keywords=[keyword(arg='check_categorical', value=Constant(value=False))]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='context_size'), List(elts=[Constant(value=0), Constant(value=3)], ctx=Load())], keywords=[]), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='start_timestamp, end_timestamp'), List(elts=[Tuple(elts=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[]), Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[])], ctx=Load()), Tuple(elts=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[]), Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-02')], keywords=[])], ctx=Load()), Tuple(elts=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[]), Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-10')], keywords=[])], ctx=Load()), Tuple(elts=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-05')], keywords=[]), Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-10')], keywords=[])], ctx=Load())], ctx=Load())], keywords=[]), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='transforms'), List(elts=[List(elts=[Call(func=Name(id='DateFlagsTransform', ctx=Load()), args=[], keywords=[])], ctx=Load()), List(elts=[Call(func=Name(id='FilterFeaturesTransform', ctx=Load()), args=[], keywords=[keyword(arg='exclude', value=List(elts=[Constant(value='regressor_exog_weekend')], ctx=Load()))])], ctx=Load()), List(elts=[Call(func=Name(id='DateFlagsTransform', ctx=Load()), args=[], keywords=[]), Call(func=Name(id='FilterFeaturesTransform', ctx=Load()), args=[], keywords=[keyword(arg='exclude', value=List(elts=[Constant(value='regressor_exog_weekend')], ctx=Load()))])], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_determine_prediction_size', args=arguments(posonlyargs=[], args=[arg(arg='start_timestamp'), arg(arg='end_timestamp'), arg(arg='expected_predic_tion_size'), arg(arg='example_tsds')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='ts', ctx=Store())], value=Name(id='example_tsds', ctx=Load())), Assign(targets=[Name(id='mixin', ctx=Store())], value=Call(func=Name(id='make_mixin', ctx=Load()), args=[], keywords=[keyword(arg='mock_determine_prediction_size', value=Constant(value=False))])), Assign(targets=[Name(id='prediction_size', ctx=Store())], value=Call(func=Attribute(value=Name(id='mixin', ctx=Load()), attr='_determine_prediction_size', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='start_timestamp', value=Name(id='start_timestamp', ctx=Load())), keyword(arg='end_timestamp', value=Name(id='end_timestamp', ctx=Load()))])), Assert(test=Compare(left=Name(id='prediction_size', ctx=Load()), ops=[Eq()], comparators=[Name(id='expected_predic_tion_size', ctx=Load())]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='start_timestamp, end_timestamp, expected_prediction_size'), List(elts=[Tuple(elts=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[]), Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[]), Constant(value=1)], ctx=Load()), Tuple(elts=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[]), Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-02')], keywords=[]), Constant(value=2)], ctx=Load()), Tuple(elts=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[]), Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-10')], keywords=[]), Constant(value=10)], ctx=Load()), Tuple(elts=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-05')], keywords=[]), Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-10')], keywords=[]), Constant(value=6)], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_predict_create_ts_called', args=arguments(posonlyargs=[], args=[arg(arg='start_timestamp'), arg(arg='end_timestamp'), arg(arg='example_tsds')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='  ǝ Ȋ ̑  ɛȘ Ͼ Ȉ̍ ɍ')), Assign(targets=[Name(id='ts', ctx=Store())], value=Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='mixin', ctx=Store())], value=Call(func=Name(id='make_mixin', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Attribute(value=Name(id='mixin', ctx=Load()), attr='_predict', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='start_timestamp', value=Name(id='start_timestamp', ctx=Load())), keyword(arg='end_timestamp', value=Name(id='end_timestamp', ctx=Load())), keyword(arg='prediction_interval', value=Constant(value=False)), keyword(arg='quantiles', value=List(elts=[], ctx=Load()))])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='mixin', ctx=Load()), attr='_create_ts', ctx=Load()), attr='assert_called_once_with', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='start_timestamp', value=Name(id='start_timestamp', ctx=Load())), keyword(arg='end_timestamp', value=Name(id='end_timestamp', ctx=Load()))]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='start_timestamp, end_timestamp'), List(elts=[Tuple(elts=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[]), Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[])], ctx=Load()), Tuple(elts=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[]), Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-02')], keywords=[])], ctx=Load()), Tuple(elts=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[]), Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-10')], keywords=[])], ctx=Load()), Tuple(elts=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-05')], keywords=[]), Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-10')], keywords=[])], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_predict_determine_prediction_size_called', args=arguments(posonlyargs=[], args=[arg(arg='start_timestamp'), arg(arg='end_timestamp'), arg(arg='example_tsds')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='̦Ο      ˱   Ģ łơ ŏȫ ȷ̢ x͔¼ ˌ')), Assign(targets=[Name(id='ts', ctx=Store())], value=Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='mixin', ctx=Store())], value=Call(func=Name(id='make_mixin', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Attribute(value=Name(id='mixin', ctx=Load()), attr='_predict', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='start_timestamp', value=Name(id='start_timestamp', ctx=Load())), keyword(arg='end_timestamp', value=Name(id='end_timestamp', ctx=Load())), keyword(arg='prediction_interval', value=Constant(value=False)), keyword(arg='quantiles', value=List(elts=[], ctx=Load()))])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='mixin', ctx=Load()), attr='_determine_prediction_size', ctx=Load()), attr='assert_called_once_with', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='start_timestamp', value=Name(id='start_timestamp', ctx=Load())), keyword(arg='end_timestamp', value=Name(id='end_timestamp', ctx=Load()))]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='start_timestamp, end_timestamp'), List(elts=[Tuple(elts=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[]), Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[])], ctx=Load()), Tuple(elts=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[]), Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-02')], keywords=[])], ctx=Load()), Tuple(elts=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[]), Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-10')], keywords=[])], ctx=Load()), Tuple(elts=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-05')], keywords=[]), Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-10')], keywords=[])], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_predict_fail_doesnt_support_prediction_interval', args=arguments(posonlyargs=[], args=[arg(arg='model_class')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ð( ɧʾ˿ϫ  \x87 \x8b ƙ  ͔     ')), Assign(targets=[Name(id='ts', ctx=Store())], value=Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[keyword(arg='spec', value=Name(id='model_class', ctx=Load()))])), Assign(targets=[Name(id='mixin', ctx=Store())], value=Call(func=Name(id='make_mixin', ctx=Load()), args=[], keywords=[keyword(arg='model', value=Name(id='model', ctx=Load()))])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='NotImplementedError', ctx=Load())], keywords=[keyword(arg='match', value=JoinedStr(values=[Constant(value='Model '), FormattedValue(value=Attribute(value=Attribute(value=Name(id='model', ctx=Load()), attr='__class__', ctx=Load()), attr='__name__', ctx=Load()), conversion=-1), Constant(value=" doesn't support prediction intervals")]))]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Attribute(value=Name(id='mixin', ctx=Load()), attr='_predict', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='start_timestamp', value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[])), keyword(arg='end_timestamp', value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-02')], keywords=[])), keyword(arg='prediction_interval', value=Constant(value=True)), keyword(arg='quantiles', value=Tuple(elts=[Constant(value=0.025), Constant(value=0.975)], ctx=Load()))]))])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='model_class'), List(elts=[Name(id='NonPredictionIntervalContextIgnorantAbstractModel', ctx=Load()), Name(id='NonPredictionIntervalContextRequiredAbstractModel', ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='_check_predict_called', args=arguments(posonlyargs=[], args=[arg(arg='spec'), arg(arg='prediction_interval'), arg(arg='quantiles'), arg(arg='check_keys')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' ʃϻ  ¾ ſ   © Üʶ       Ă')), Assign(targets=[Name(id='ts', ctx=Store())], value=Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[keyword(arg='spec', value=Name(id='spec', ctx=Load()))])), Assign(targets=[Name(id='mixin', ctx=Store())], value=Call(func=Name(id='make_mixin', ctx=Load()), args=[], keywords=[keyword(arg='model', value=Name(id='model', ctx=Load()))])), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Attribute(value=Name(id='mixin', ctx=Load()), attr='_predict', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='start_timestamp', value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[])), keyword(arg='end_timestamp', value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), args=[Constant(value='2020-01-02')], keywords=[])), keyword(arg='prediction_interval', value=Name(id='prediction_interval', ctx=Load())), keyword(arg='quantiles', value=Name(id='quantiles', ctx=Load()))])), Assign(targets=[Name(id='expected_ts', ctx=Store())], value=Attribute(value=Attribute(value=Name(id='mixin', ctx=Load()), attr='_create_ts', ctx=Load()), attr='return_value', ctx=Load())), Assign(targets=[Name(id='expected_predic_tion_size', ctx=Store())], value=Attribute(value=Attribute(value=Name(id='mixin', ctx=Load()), attr='_determine_prediction_size', ctx=Load()), attr='return_value', ctx=Load())), Assign(targets=[Name(id='called_with_full', ctx=Store())], value=Call(func=Name(id='dict', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='expected_ts', ctx=Load())), keyword(arg='prediction_size', value=Name(id='expected_predic_tion_size', ctx=Load())), keyword(arg='prediction_interval', value=Name(id='prediction_interval', ctx=Load())), keyword(arg='quantiles', value=Name(id='quantiles', ctx=Load()))])), Assign(targets=[Name(id='called_with_', ctx=Store())], value=DictComp(key=Name(id='key', ctx=Load()), value=Name(id='value', ctx=Load()), generators=[comprehension(target=Tuple(elts=[Name(id='key', ctx=Store()), Name(id='value', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Name(id='called_with_full', ctx=Load()), attr='items', ctx=Load()), args=[], keywords=[]), ifs=[Compare(left=Name(id='key', ctx=Load()), ops=[In()], comparators=[Name(id='check_keys', ctx=Load())])], is_async=0)])), Expr(value=Call(func=Attribute(value=Attribute(value=Attribute(value=Name(id='mixin', ctx=Load()), attr='model', ctx=Load()), attr='predict', ctx=Load()), attr='assert_called_once_with', ctx=Load()), args=[], keywords=[keyword(value=Name(id='called_with_', ctx=Load()))])), Assert(test=Compare(left=Name(id='result', ctx=Load()), ops=[Eq()], comparators=[Attribute(value=Attribute(value=Attribute(value=Name(id='mixin', ctx=Load()), attr='model', ctx=Load()), attr='predict', ctx=Load()), attr='return_value', ctx=Load())]))], decorator_list=[]), FunctionDef(name='test_predict_model_predict_called_non_prediction_interval_context_ignorant', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Call(func=Name(id='_check_predict_called', ctx=Load()), args=[], keywords=[keyword(arg='spec', value=Name(id='NonPredictionIntervalContextIgnorantAbstractModel', ctx=Load())), keyword(arg='prediction_interval', value=Constant(value=False)), keyword(arg='quantiles', value=Tuple(elts=[], ctx=Load())), keyword(arg='check_keys', value=List(elts=[Constant(value='ts')], ctx=Load()))]))], decorator_list=[]), FunctionDef(name='test_predict_model_predict_called_non_prediction_interval_context_required', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='   ̩ȯ  ʿ|          ')), Expr(value=Call(func=Name(id='_check_predict_called', ctx=Load()), args=[], keywords=[keyword(arg='spec', value=Name(id='NonPredictionIntervalContextRequiredAbstractModel', ctx=Load())), keyword(arg='prediction_interval', value=Constant(value=False)), keyword(arg='quantiles', value=Tuple(elts=[], ctx=Load())), keyword(arg='check_keys', value=List(elts=[Constant(value='ts'), Constant(value='prediction_size')], ctx=Load()))]))], decorator_list=[]), FunctionDef(name='test_predict_model_predict_called_prediction_interval_context_ignorant', args=arguments(posonlyargs=[], args=[arg(arg='prediction_interval'), arg(arg='quantiles')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='§  ðǨĹ  Ń ')), Expr(value=Call(func=Name(id='_check_predict_called', ctx=Load()), args=[], keywords=[keyword(arg='spec', value=Name(id='PredictionIntervalContextIgnorantAbstractModel', ctx=Load())), keyword(arg='prediction_interval', value=Constant(value=False)), keyword(arg='quantiles', value=Tuple(elts=[], ctx=Load())), keyword(arg='check_keys', value=List(elts=[Constant(value='ts'), Constant(value='prediction_interval'), Constant(value='quantiles')], ctx=Load()))]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='quantiles'), List(elts=[Tuple(elts=[Constant(value=0.025), Constant(value=0.975)], ctx=Load()), Tuple(elts=[Constant(value=0.5)], ctx=Load()), Tuple(elts=[], ctx=Load())], ctx=Load())], keywords=[]), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='prediction_interval'), List(elts=[Constant(value=False), Constant(value=True)], ctx=Load())], keywords=[])]), FunctionDef(name='test_predict_model_predict_called_prediction_interval_context_required', args=arguments(posonlyargs=[], args=[arg(arg='prediction_interval'), arg(arg='quantiles')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Call(func=Name(id='_check_predict_called', ctx=Load()), args=[], keywords=[keyword(arg='spec', value=Name(id='PredictionIntervalContextRequiredAbstractModel', ctx=Load())), keyword(arg='prediction_interval', value=Constant(value=False)), keyword(arg='quantiles', value=Tuple(elts=[], ctx=Load())), keyword(arg='check_keys', value=List(elts=[Constant(value='ts'), Constant(value='prediction_size'), Constant(value='prediction_interval'), Constant(value='quantiles')], ctx=Load()))]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='quantiles'), List(elts=[Tuple(elts=[Constant(value=0.025), Constant(value=0.975)], ctx=Load()), Tuple(elts=[Constant(value=0.5)], ctx=Load()), Tuple(elts=[], ctx=Load())], ctx=Load())], keywords=[]), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='prediction_interval'), List(elts=[Constant(value=False), Constant(value=True)], ctx=Load())], keywords=[])])], type_ignores=[])