Module(body=[ImportFrom(module='unittest.mock', names=[alias(name='MagicMock')], level=0), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pytest')]), ImportFrom(module='etna.metrics', names=[alias(name='MAE')], level=0), ImportFrom(module='etna.models.nn', names=[alias(name='RNNModel')], level=0), ImportFrom(module='etna.models.nn.rnn', names=[alias(name='RNNNet')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='StandardScalerTransform')], level=0), FunctionDef(name='test_rnn_model_run_weekly_overfit_with_scaler', args=arguments(posonlyargs=[], args=[arg(arg='ts_dataset_weekly_function_with_horizon'), arg(arg='horizon')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Giv~̖ʶen: I haveʽ"͢ dűat̵ä́fȤ˾rǺamĤȕe w½ʵit#h 2 ɲsegments ÒwiΙth ͕weʧeͪkly season̋aʋǔliϬty wʊζitϜh ʨk͇nownͷ futˣurȃe\nWh\x93en: ďI use scale 0tran\x8fϜsfɬormaĔtions£\nThen: I\u0380Ε get ~{Ȍhoriέzon} pϕ˕eriƭwodsɓȣ p̪eǮr dΦataseţt as aϞ ʏfoʌrecastȒ andʷ they \x91"Ȇthe same\x7fÄ"> Γaŝsμ past')), Assign(targets=[Tuple(elts=[Name(id='ts_train', ctx=Store()), Name(id='ts_test', ctx=Store())], ctx=Store())], value=Call(func=Name(id='ts_dataset_weekly_function_with_horizon', ctx=Load()), args=[Name(id='horizon', ctx=Load())], keywords=[])), Assign(targets=[Name(id='std', ctx=Store())], value=Call(func=Name(id='StandardScalerTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target'))])), Expr(value=Call(func=Attribute(value=Name(id='ts_train', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='std', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='encoder_lengthF', ctx=Store())], value=Constant(value=14)), Assign(targets=[Name(id='decoder_length', ctx=Store())], value=Constant(value=14)), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='RNNModel', ctx=Load()), args=[], keywords=[keyword(arg='input_size', value=Constant(value=1)), keyword(arg='encoder_length', value=Name(id='encoder_lengthF', ctx=Load())), keyword(arg='decoder_length', value=Name(id='decoder_length', ctx=Load())), keyword(arg='trainer_params', value=Call(func=Name(id='dict', ctx=Load()), args=[], keywords=[keyword(arg='max_epochs', value=Constant(value=100))]))])), Assign(targets=[Name(id='future', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts_train', ctx=Load()), attr='make_future', ctx=Load()), args=[Name(id='horizon', ctx=Load()), Name(id='encoder_lengthF', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='ts_train', ctx=Load())], keywords=[])), Assign(targets=[Name(id='future', ctx=Store())], value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='forecast', ctx=Load()), args=[Name(id='future', ctx=Load())], keywords=[keyword(arg='prediction_size', value=Name(id='horizon', ctx=Load()))])), Assign(targets=[Name(id='mae', ctx=Store())], value=Call(func=Name(id='MAE', ctx=Load()), args=[Constant(value='macro')], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='mae', ctx=Load()), args=[Name(id='ts_test', ctx=Load()), Name(id='future', ctx=Load())], keywords=[]), ops=[Lt()], comparators=[Constant(value=0.06)]))], decorator_list=[Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='long_2', ctx=Load()), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='horizon'), List(elts=[Constant(value=8), Constant(value=13), Constant(value=15)], ctx=Load())], keywords=[])]), FunctionDef(name='test_rnn_make_samples', args=arguments(posonlyargs=[], args=[arg(arg='example_df')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='rnn_module', ctx=Store())], value=Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='encoder_lengthF', ctx=Store())], value=Constant(value=8)), Assign(targets=[Name(id='decoder_length', ctx=Store())], value=Constant(value=4)), Assign(targets=[Name(id='ts_samples', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[Call(func=Attribute(value=Name(id='RNNNet', ctx=Load()), attr='make_samples', ctx=Load()), args=[Name(id='rnn_module', ctx=Load())], keywords=[keyword(arg='df', value=Name(id='example_df', ctx=Load())), keyword(arg='encoder_length', value=Name(id='encoder_lengthF', ctx=Load())), keyword(arg='decoder_length', value=Name(id='decoder_length', ctx=Load()))])], keywords=[])), Assign(targets=[Name(id='first_sample', ctx=Store())], value=Subscript(value=Name(id='ts_samples', ctx=Load()), slice=Constant(value=0), ctx=Load())), Assign(targets=[Name(id='second_sample', ctx=Store())], value=Subscript(value=Name(id='ts_samples', ctx=Load()), slice=Constant(value=1), ctx=Load())), Assert(test=Compare(left=Subscript(value=Name(id='first_sample', ctx=Load()), slice=Constant(value='segment'), ctx=Load()), ops=[Eq()], comparators=[Constant(value='segment_1')])), Assert(test=Compare(left=Attribute(value=Subscript(value=Name(id='first_sample', ctx=Load()), slice=Constant(value='encoder_real'), ctx=Load()), attr='shape', ctx=Load()), ops=[Eq()], comparators=[Tuple(elts=[BinOp(left=Name(id='encoder_lengthF', ctx=Load()), op=Sub(), right=Constant(value=1)), Constant(value=1)], ctx=Load())])), Assert(test=Compare(left=Attribute(value=Subscript(value=Name(id='first_sample', ctx=Load()), slice=Constant(value='decoder_real'), ctx=Load()), attr='shape', ctx=Load()), ops=[Eq()], comparators=[Tuple(elts=[Name(id='decoder_length', ctx=Load()), Constant(value=1)], ctx=Load())])), Assert(test=Compare(left=Attribute(value=Subscript(value=Name(id='first_sample', ctx=Load()), slice=Constant(value='encoder_target'), ctx=Load()), attr='shape', ctx=Load()), ops=[Eq()], comparators=[Tuple(elts=[BinOp(left=Name(id='encoder_lengthF', ctx=Load()), op=Sub(), right=Constant(value=1)), Constant(value=1)], ctx=Load())])), Assert(test=Compare(left=Attribute(value=Subscript(value=Name(id='first_sample', ctx=Load()), slice=Constant(value='decoder_target'), ctx=Load()), attr='shape', ctx=Load()), ops=[Eq()], comparators=[Tuple(elts=[Name(id='decoder_length', ctx=Load()), Constant(value=1)], ctx=Load())])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='testing', ctx=Load()), attr='assert_equal', ctx=Load()), args=[Subscript(value=Attribute(value=Subscript(value=Name(id='example_df', ctx=Load()), slice=List(elts=[Constant(value='target')], ctx=Load()), ctx=Load()), attr='iloc', ctx=Load()), slice=Slice(upper=BinOp(left=Name(id='encoder_lengthF', ctx=Load()), op=Sub(), right=Constant(value=1))), ctx=Load()), Subscript(value=Name(id='first_sample', ctx=Load()), slice=Constant(value='encoder_real'), ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='testing', ctx=Load()), attr='assert_equal', ctx=Load()), args=[Subscript(value=Attribute(value=Subscript(value=Name(id='example_df', ctx=Load()), slice=List(elts=[Constant(value='target')], ctx=Load()), ctx=Load()), attr='iloc', ctx=Load()), slice=Slice(lower=Constant(value=1), upper=Name(id='encoder_lengthF', ctx=Load())), ctx=Load()), Subscript(value=Name(id='second_sample', ctx=Load()), slice=Constant(value='encoder_real'), ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='test_context_size', args=arguments(posonlyargs=[], args=[arg(arg='encoder_lengthF')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='encoder_lengthF', ctx=Store())], value=Name(id='encoder_lengthF', ctx=Load())), Assign(targets=[Name(id='decoder_length', ctx=Store())], value=Name(id='encoder_lengthF', ctx=Load())), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='RNNModel', ctx=Load()), args=[], keywords=[keyword(arg='input_size', value=Constant(value=1)), keyword(arg='encoder_length', value=Name(id='encoder_lengthF', ctx=Load())), keyword(arg='decoder_length', value=Name(id='decoder_length', ctx=Load())), keyword(arg='trainer_params', value=Call(func=Name(id='dict', ctx=Load()), args=[], keywords=[keyword(arg='max_epochs', value=Constant(value=100))]))])), Assert(test=Compare(left=Attribute(value=Name(id='model', ctx=Load()), attr='context_size', ctx=Load()), ops=[Eq()], comparators=[Name(id='encoder_lengthF', ctx=Load())]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='encoder_length'), List(elts=[Constant(value=1), Constant(value=2), Constant(value=10)], ctx=Load())], keywords=[])])], type_ignores=[])