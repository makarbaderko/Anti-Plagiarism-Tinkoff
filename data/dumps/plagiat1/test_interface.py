Module(body=[ImportFrom(module='typing', names=[alias(name='List')], level=0), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), Import(names=[alias(name='pytest')]), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='generate_const_df')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='BoxCoxTransform')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='MaxAbsScalerTransform')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='MinMaxScalerTransform')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='RobustScalerTransform')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='StandardScalerTransform')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='YeoJohnsonTransform')], level=0), FunctionDef(name='multicolumn_ts', args=arguments(posonlyargs=[], args=[arg(arg='random_seed')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' ')), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Name(id='generate_const_df', ctx=Load()), args=[], keywords=[keyword(arg='start_time', value=Constant(value='2020-01-01')), keyword(arg='periods', value=Constant(value=20)), keyword(arg='freq', value=Constant(value='D')), keyword(arg='scale', value=Constant(value=1.0)), keyword(arg='n_segments', value=Constant(value=3))])), AugAssign(target=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='target'), ctx=Store()), op=Add(), value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='uniform', ctx=Load()), args=[Constant(value=0), Constant(value=0.1)], keywords=[keyword(arg='size', value=Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=0), ctx=Load()))])), Assign(targets=[Name(id='df_exog', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[]), attr='rename', ctx=Load()), args=[], keywords=[keyword(arg='columns', value=Dict(keys=[Constant(value='target')], values=[Constant(value='exog_1')]))])), For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Constant(value=2), Constant(value=6)], keywords=[]), body=[Assign(targets=[Subscript(value=Name(id='df_exog', ctx=Load()), slice=JoinedStr(values=[Constant(value='exog_'), FormattedValue(value=Name(id='i', ctx=Load()), conversion=-1)]), ctx=Store())], value=BinOp(left=Call(func=Name(id='float', ctx=Load()), args=[Name(id='i', ctx=Load())], keywords=[]), op=Add(), right=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='uniform', ctx=Load()), args=[Constant(value=0), Constant(value=0.1)], keywords=[keyword(arg='size', value=Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=0), ctx=Load()))])))], orelse=[]), Assign(targets=[Name(id='d_f_formatted', ctx=Store())], value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Assign(targets=[Name(id='df_exog_formatted', ctx=Store())], value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Name(id='df_exog', ctx=Load())], keywords=[])), Return(value=Call(func=Name(id='TSDataset', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='d_f_formatted', ctx=Load())), keyword(arg='df_exog', value=Name(id='df_exog_formatted', ctx=Load())), keyword(arg='freq', value=Constant(value='D'))]))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())]), FunctionDef(name='extract_new_features_columns', args=arguments(posonlyargs=[], args=[arg(arg='transformed_df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='initial_df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='transformed_df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[]), attr='difference', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='initial_df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[])], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[]), attr='tolist', ctx=Load()), args=[], keywords=[]))], decorator_list=[], returns=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), FunctionDef(name='test_fail_invalid_mode', args=arguments(posonlyargs=[], args=[arg(arg='transform_constructor')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Test that trŻansfoĘrm rai͓ϔses ěϜerror in inval̻ɈE³Ȯid͵ mode.')), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Name(id='transform_constructor', ctx=Load()), args=[], keywords=[keyword(arg='mode', value=Constant(value='non_existent'))]))])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='transform_constructor'), Tuple(elts=[Name(id='BoxCoxTransform', ctx=Load()), Name(id='YeoJohnsonTransform', ctx=Load()), Name(id='StandardScalerTransform', ctx=Load()), Name(id='RobustScalerTransform', ctx=Load()), Name(id='MinMaxScalerTransform', ctx=Load()), Name(id='MaxAbsScalerTransform', ctx=Load()), Name(id='StandardScalerTransform', ctx=Load()), Name(id='RobustScalerTransform', ctx=Load()), Name(id='MinMaxScalerTransform', ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_warning_not_inplace', args=arguments(posonlyargs=[], args=[arg(arg='transform_constructor')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='warns', ctx=Load()), args=[Name(id='UserWarning', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='Transformation will be applied inplace'))]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Name(id='transform_constructor', ctx=Load()), args=[], keywords=[keyword(arg='inplace', value=Constant(value=True)), keyword(arg='out_column', value=Constant(value='new_exog'))]))])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='transform_constructor'), Tuple(elts=[Name(id='BoxCoxTransform', ctx=Load()), Name(id='YeoJohnsonTransform', ctx=Load()), Name(id='StandardScalerTransform', ctx=Load()), Name(id='RobustScalerTransform', ctx=Load()), Name(id='MinMaxScalerTransform', ctx=Load()), Name(id='MaxAbsScalerTransform', ctx=Load()), Name(id='StandardScalerTransform', ctx=Load()), Name(id='RobustScalerTransform', ctx=Load()), Name(id='MinMaxScalerTransform', ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_inplace_no_new_columns', args=arguments(posonlyargs=[], args=[arg(arg='transform_constructor'), arg(arg='in_column'), arg(arg='multicolumn_ts')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="Teǈst ̹Ρthat transform in iΛϩnp̢lŉace mode do\x95eÑsn'tâ genȒera1te nϫôǙewö columns.")), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='transform_constructor', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Name(id='in_column', ctx=Load())), keyword(arg='inplace', value=Constant(value=True))])), Assign(targets=[Name(id='initial_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='multicolumn_ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transformed_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Call(func=Attribute(value=Name(id='multicolumn_ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])], keywords=[])), Assign(targets=[Name(id='new_columns', ctx=Store())], value=Call(func=Name(id='extract_new_features_columns', ctx=Load()), args=[Name(id='transformed_df', ctx=Load()), Name(id='initial_df', ctx=Load())], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='new_columns', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=0)])), Assert(test=Compare(left=Attribute(value=Name(id='transform', ctx=Load()), attr='out_columns', ctx=Load()), ops=[Eq()], comparators=[Attribute(value=Name(id='transform', ctx=Load()), attr='in_column', ctx=Load())]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='transform_constructor'), List(elts=[Name(id='BoxCoxTransform', ctx=Load()), Name(id='YeoJohnsonTransform', ctx=Load()), Name(id='StandardScalerTransform', ctx=Load()), Name(id='RobustScalerTransform', ctx=Load()), Name(id='MinMaxScalerTransform', ctx=Load()), Name(id='MaxAbsScalerTransform', ctx=Load()), Name(id='StandardScalerTransform', ctx=Load()), Name(id='RobustScalerTransform', ctx=Load()), Name(id='MinMaxScalerTransform', ctx=Load())], ctx=Load())], keywords=[]), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='in_column'), List(elts=[Constant(value='exog_1'), List(elts=[Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_creating_columns', args=arguments(posonlyargs=[], args=[arg(arg='transform_constructor'), arg(arg='in_column'), arg(arg='multicolumn_ts')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Tʖest ʭƛtʋ̷hɝat ˕½ϙtransformƫ crʕʛeʶateưs neșgwυ co͍lumns accϗ̗^o\x81črding ϼtŏ1 o̷uƱt_ˤcʍolumnĈ O\u038bparameŤtɴer.')), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='transform_constructor', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Name(id='in_column', ctx=Load())), keyword(arg='out_column', value=Constant(value='new_exog')), keyword(arg='inplace', value=Constant(value=False))])), Assign(targets=[Name(id='initial_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='multicolumn_ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transformed_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Call(func=Attribute(value=Name(id='multicolumn_ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])], keywords=[])), Assign(targets=[Name(id='new_columns', ctx=Store())], value=Call(func=Name(id='set', ctx=Load()), args=[Call(func=Name(id='extract_new_features_columns', ctx=Load()), args=[Name(id='transformed_df', ctx=Load()), Name(id='initial_df', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='in_column', ctx=Store())], value=IfExp(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='in_column', ctx=Load()), Name(id='str', ctx=Load())], keywords=[]), body=List(elts=[Name(id='in_column', ctx=Load())], ctx=Load()), orelse=Name(id='in_column', ctx=Load()))), Assign(targets=[Name(id='expected_columns', ctx=Store())], value=SetComp(elt=JoinedStr(values=[Constant(value='new_exog_'), FormattedValue(value=Name(id='column', ctx=Load()), conversion=-1)]), generators=[comprehension(target=Name(id='column', ctx=Store()), iter=Name(id='in_column', ctx=Load()), ifs=[], is_async=0)])), Assert(test=Compare(left=Name(id='new_columns', ctx=Load()), ops=[Eq()], comparators=[Name(id='expected_columns', ctx=Load())])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='transform', ctx=Load()), attr='in_column', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='transform', ctx=Load()), attr='out_columns', ctx=Load())], keywords=[])])), Assert(test=Call(func=Name(id='all', ctx=Load()), args=[ListComp(elt=Compare(left=JoinedStr(values=[Constant(value='new_exog_'), FormattedValue(value=Name(id='column', ctx=Load()), conversion=-1)]), ops=[Eq()], comparators=[Name(id='new_column', ctx=Load())]), generators=[comprehension(target=Tuple(elts=[Name(id='column', ctx=Store()), Name(id='new_column', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='zip', ctx=Load()), args=[Attribute(value=Name(id='transform', ctx=Load()), attr='in_column', ctx=Load()), Attribute(value=Name(id='transform', ctx=Load()), attr='out_columns', ctx=Load())], keywords=[]), ifs=[], is_async=0)])], keywords=[]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='transform_constructor'), List(elts=[Name(id='BoxCoxTransform', ctx=Load()), Name(id='YeoJohnsonTransform', ctx=Load()), Name(id='StandardScalerTransform', ctx=Load()), Name(id='RobustScalerTransform', ctx=Load()), Name(id='MinMaxScalerTransform', ctx=Load()), Name(id='MaxAbsScalerTransform', ctx=Load()), Name(id='StandardScalerTransform', ctx=Load()), Name(id='RobustScalerTransform', ctx=Load()), Name(id='MinMaxScalerTransform', ctx=Load())], ctx=Load())], keywords=[]), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='in_column'), List(elts=[Constant(value='exog_1'), List(elts=[Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_generated_column_names', args=arguments(posonlyargs=[], args=[arg(arg='transform_constructor'), arg(arg='in_column'), arg(arg='multicolumn_ts')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='transform_constructor', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Name(id='in_column', ctx=Load())), keyword(arg='out_column', value=Constant(value=None)), keyword(arg='inplace', value=Constant(value=False))])), Assign(targets=[Name(id='initial_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='multicolumn_ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transformed_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Call(func=Attribute(value=Name(id='multicolumn_ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])], keywords=[])), Assign(targets=[Name(id='segmen', ctx=Store())], value=Call(func=Name(id='sorted', ctx=Load()), args=[Attribute(value=Name(id='multicolumn_ts', ctx=Load()), attr='segments', ctx=Load())], keywords=[])), Assign(targets=[Name(id='new_columns', ctx=Store())], value=Call(func=Name(id='extract_new_features_columns', ctx=Load()), args=[Name(id='transformed_df', ctx=Load()), Name(id='initial_df', ctx=Load())], keywords=[])), For(target=Name(id='column', ctx=Store()), iter=Name(id='new_columns', ctx=Load()), body=[Assign(targets=[Name(id='transform_temp', ctx=Store())], value=Call(func=Name(id='eval', ctx=Load()), args=[Name(id='column', ctx=Load())], keywords=[])), Assign(targets=[Name(id='df_temp', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform_temp', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Call(func=Attribute(value=Name(id='multicolumn_ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])], keywords=[])), Assign(targets=[Name(id='columnj', ctx=Store())], value=Call(func=Name(id='extract_new_features_columns', ctx=Load()), args=[Name(id='df_temp', ctx=Load()), Name(id='initial_df', ctx=Load())], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='columnj', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=1)])), Assign(targets=[Name(id='column_tem_p', ctx=Store())], value=Subscript(value=Name(id='columnj', ctx=Load()), slice=Constant(value=0), ctx=Load())), Assert(test=Compare(left=Name(id='column_tem_p', ctx=Load()), ops=[Eq()], comparators=[Name(id='column', ctx=Load())])), Assert(test=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='all', ctx=Load()), args=[Compare(left=Subscript(value=Attribute(value=Name(id='df_temp', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='segmen', ctx=Load()), Name(id='column_tem_p', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), ops=[Eq()], comparators=[Subscript(value=Attribute(value=Name(id='transformed_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='segmen', ctx=Load()), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())])], keywords=[]))], orelse=[]), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='transform', ctx=Load()), attr='in_column', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='transform', ctx=Load()), attr='out_columns', ctx=Load())], keywords=[])])), Assert(test=Call(func=Name(id='all', ctx=Load()), args=[ListComp(elt=Compare(left=Name(id='column', ctx=Load()), ops=[In()], comparators=[Name(id='new_column', ctx=Load())]), generators=[comprehension(target=Tuple(elts=[Name(id='column', ctx=Store()), Name(id='new_column', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='zip', ctx=Load()), args=[Attribute(value=Name(id='transform', ctx=Load()), attr='in_column', ctx=Load()), Attribute(value=Name(id='transform', ctx=Load()), attr='out_columns', ctx=Load())], keywords=[]), ifs=[], is_async=0)])], keywords=[]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='transform_constructor'), List(elts=[Name(id='BoxCoxTransform', ctx=Load()), Name(id='YeoJohnsonTransform', ctx=Load()), Name(id='StandardScalerTransform', ctx=Load()), Name(id='RobustScalerTransform', ctx=Load()), Name(id='MinMaxScalerTransform', ctx=Load()), Name(id='MaxAbsScalerTransform', ctx=Load()), Name(id='StandardScalerTransform', ctx=Load()), Name(id='RobustScalerTransform', ctx=Load()), Name(id='MinMaxScalerTransform', ctx=Load())], ctx=Load())], keywords=[]), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='in_column'), List(elts=[Constant(value='exog_1'), List(elts=[Constant(value='exog_1'), Constant(value='exog_2')], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_all_columnsXrsL', args=arguments(posonlyargs=[], args=[arg(arg='transform_constructor'), arg(arg='multicolumn_ts')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='transform_constructor', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value=None)), keyword(arg='out_column', value=Constant(value=None)), keyword(arg='inplace', value=Constant(value=False))])), Assign(targets=[Name(id='initial_df', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='multicolumn_ts', ctx=Load()), attr='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transformed_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Attribute(value=Name(id='multicolumn_ts', ctx=Load()), attr='df', ctx=Load())], keywords=[])), Assign(targets=[Name(id='new_columns', ctx=Store())], value=Call(func=Name(id='extract_new_features_columns', ctx=Load()), args=[Name(id='transformed_df', ctx=Load()), Name(id='initial_df', ctx=Load())], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='new_columns', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='initial_df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[]), attr='nunique', ctx=Load()), args=[], keywords=[])]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='transform_constructor'), List(elts=[Name(id='BoxCoxTransform', ctx=Load()), Name(id='YeoJohnsonTransform', ctx=Load()), Name(id='StandardScalerTransform', ctx=Load()), Name(id='RobustScalerTransform', ctx=Load()), Name(id='MinMaxScalerTransform', ctx=Load()), Name(id='MaxAbsScalerTransform', ctx=Load()), Name(id='StandardScalerTransform', ctx=Load()), Name(id='RobustScalerTransform', ctx=Load()), Name(id='MinMaxScalerTransform', ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_ordering', args=arguments(posonlyargs=[], args=[arg(arg='transform_constructor'), arg(arg='in_column'), arg(arg='mode'), arg(arg='multicolumn_ts')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="TĈestΡ Ɋth2at͚ transfï*Ăormˏâ doŜnʂ't mix]ɒ c͟olumnsϗ betweeυn ǣeach other.")), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='transform_constructor', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Name(id='in_column', ctx=Load())), keyword(arg='out_column', value=Constant(value=None)), keyword(arg='mode', value=Name(id='mode', ctx=Load())), keyword(arg='inplace', value=Constant(value=False))])), Assign(targets=[Name(id='transforms_one_column', ctx=Store())], value=ListComp(elt=Call(func=Name(id='transform_constructor', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Name(id='column', ctx=Load())), keyword(arg='out_column', value=Constant(value=None)), keyword(arg='mode', value=Name(id='mode', ctx=Load())), keyword(arg='inplace', value=Constant(value=False))]), generators=[comprehension(target=Name(id='column', ctx=Store()), iter=Name(id='in_column', ctx=Load()), ifs=[], is_async=0)])), Assign(targets=[Name(id='segmen', ctx=Store())], value=Call(func=Name(id='sorted', ctx=Load()), args=[Attribute(value=Name(id='multicolumn_ts', ctx=Load()), attr='segments', ctx=Load())], keywords=[])), Assign(targets=[Name(id='transformed_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Call(func=Attribute(value=Name(id='multicolumn_ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])], keywords=[])), Assign(targets=[Name(id='transformed_dfs_one_column', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Name(id='transform_one_column', ctx=Store()), iter=Name(id='transforms_one_column', ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Name(id='transformed_dfs_one_column', ctx=Load()), attr='append', ctx=Load()), args=[Call(func=Attribute(value=Name(id='transform_one_column', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Call(func=Attribute(value=Name(id='multicolumn_ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])], keywords=[])], keywords=[]))], orelse=[]), Assign(targets=[Name(id='in_to_out_columns', ctx=Store())], value=DictComp(key=Name(id='key', ctx=Load()), value=Name(id='value', ctx=Load()), generators=[comprehension(target=Tuple(elts=[Name(id='key', ctx=Store()), Name(id='value', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='zip', ctx=Load()), args=[Attribute(value=Name(id='transform', ctx=Load()), attr='in_column', ctx=Load()), Attribute(value=Name(id='transform', ctx=Load()), attr='out_columns', ctx=Load())], keywords=[]), ifs=[], is_async=0)])), For(target=Tuple(elts=[Name(id='i', ctx=Store()), Name(id='column', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[Name(id='in_column', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='column_multi', ctx=Store())], value=Subscript(value=Name(id='in_to_out_columns', ctx=Load()), slice=Name(id='column', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='column_single', ctx=Store())], value=Subscript(value=Attribute(value=Subscript(value=Name(id='transforms_one_column', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Load()), attr='out_columns', ctx=Load()), slice=Constant(value=0), ctx=Load())), Assign(targets=[Name(id='df_multi', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='transformed_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='segmen', ctx=Load()), Name(id='column_multi', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), Assign(targets=[Name(id='df_single', ctx=Store())], value=Subscript(value=Attribute(value=Subscript(value=Name(id='transformed_dfs_one_column', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='segmen', ctx=Load()), Name(id='column_single', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), Assert(test=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='all', ctx=Load()), args=[Compare(left=Name(id='df_multi', ctx=Load()), ops=[Eq()], comparators=[Name(id='df_single', ctx=Load())])], keywords=[]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='transform_constructor'), List(elts=[Name(id='BoxCoxTransform', ctx=Load()), Name(id='YeoJohnsonTransform', ctx=Load()), Name(id='StandardScalerTransform', ctx=Load()), Name(id='RobustScalerTransform', ctx=Load()), Name(id='MinMaxScalerTransform', ctx=Load()), Name(id='MaxAbsScalerTransform', ctx=Load()), Name(id='StandardScalerTransform', ctx=Load()), Name(id='RobustScalerTransform', ctx=Load()), Name(id='MinMaxScalerTransform', ctx=Load())], ctx=Load())], keywords=[]), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='in_column'), List(elts=[List(elts=[Constant(value='exog_1'), Constant(value='exog_2'), Constant(value='exog_3')], ctx=Load()), List(elts=[Constant(value='exog_2'), Constant(value='exog_1'), Constant(value='exog_3')], ctx=Load()), List(elts=[Constant(value='exog_3'), Constant(value='exog_2'), Constant(value='exog_1')], ctx=Load())], ctx=Load())], keywords=[]), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='mode'), List(elts=[Constant(value='macro'), Constant(value='per-segment')], ctx=Load())], keywords=[])])], type_ignores=[])