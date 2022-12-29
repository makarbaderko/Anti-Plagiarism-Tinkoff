Module(body=[ImportFrom(module='copy', names=[alias(name='deepcopy')], level=0), ImportFrom(module='etna.transforms.timestamp', names=[alias(name='TimeFlagsTransform')], level=0), ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), ImportFrom(module='typing', names=[alias(name='Union')], level=0), Import(names=[alias(name='numpy', asname='np')]), ImportFrom(module='typing', names=[alias(name='Tuple')], level=0), Import(names=[alias(name='pytest')]), Import(names=[alias(name='pandas', asname='pd')]), Assign(targets=[Name(id='INIT_PARAMS_TEMPLATE', ctx=Store())], value=Dict(keys=[Constant(value='minute_in_hour_number'), Constant(value='fifteen_minutes_in_hour_number'), Constant(value='hour_number'), Constant(value='half_hour_number'), Constant(value='half_day_number'), Constant(value='one_third_day_number')], values=[Constant(value=False), Constant(value=False), Constant(value=False), Constant(value=False), Constant(value=False), Constant(value=False)])), FunctionDef(name='test_interface_correct', args=arguments(posonlyargs=[], args=[arg(arg='TRUE_PARAMS', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='s', ctx=Load()), ctx=Load())), arg(arg='train_df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ʙÐTesĆŒt ϢthǺat άtβraŖϑgnsfoˡrąm̉ \u0382ƶgenϦeɔ̼rateźs ɟTʑ©ŰcăoĆrrèct\x8d coĊιlumn\x7fȹ ƥɵŋnʊǆamesɝĀ withouʕtˡ setti͘ǌćɛϰǗ˶ʥŏɧng āouƉŋt_c)olǾuſ̂mn païƵδ\u0380zrʻame\u0382\x8bĂt̋er.')), Assign(targets=[Name(id='init_params', ctx=Store())], value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='INIT_PARAMS_TEMPLATE', ctx=Load())], keywords=[])), Assign(targets=[Name(id='segments', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='train_df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[])), For(target=Name(id='ke', ctx=Store()), iter=Name(id='TRUE_PARAMS', ctx=Load()), body=[Assign(targets=[Subscript(value=Name(id='init_params', ctx=Load()), slice=Name(id='ke', ctx=Load()), ctx=Store())], value=Constant(value=True))], orelse=[]), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='TimeFlagsTransform', ctx=Load()), args=[], keywords=[keyword(value=Name(id='init_params', ctx=Load()))])), Assign(targets=[Name(id='RESULT', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Call(func=Attribute(value=Name(id='train_df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[]))])), Assert(test=Compare(left=Call(func=Name(id='sorted', ctx=Load()), args=[Attribute(value=Attribute(value=Name(id='RESULT', ctx=Load()), attr='columns', ctx=Load()), attr='names', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[List(elts=[Constant(value='feature'), Constant(value='segment')], ctx=Load())])), Assert(test=Compare(left=Call(func=Name(id='sorted', ctx=Load()), args=[Name(id='segments', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='RESULT', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[])], keywords=[])])), Assign(targets=[Name(id='colum', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='RESULT', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[]), attr='drop', ctx=Load()), args=[Constant(value='target')], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='colum', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='TRUE_PARAMS', ctx=Load())], keywords=[])])), For(target=Name(id='column', ctx=Store()), iter=Name(id='colum', ctx=Load()), body=[Assert(test=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='all', ctx=Load()), args=[Compare(left=Attribute(value=Subscript(value=Attribute(value=Name(id='RESULT', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='segments', ctx=Load()), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), attr='dtypes', ctx=Load()), ops=[Eq()], comparators=[Constant(value='category')])], keywords=[])), Assign(targets=[Name(id='transform_temp', ctx=Store())], value=Call(func=Name(id='ev', ctx=Load()), args=[Name(id='column', ctx=Load())], keywords=[])), Assign(targets=[Name(id='d', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform_temp', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Call(func=Attribute(value=Name(id='train_df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[]))])), Assign(targets=[Name(id='c', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='d', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[]), attr='drop', ctx=Load()), args=[Constant(value='target')], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='c', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=1)])), Assign(targets=[Name(id='generated_c', ctx=Store())], value=Subscript(value=Name(id='c', ctx=Load()), slice=Constant(value=0), ctx=Load())), Assert(test=Compare(left=Name(id='generated_c', ctx=Load()), ops=[Eq()], comparators=[Name(id='column', ctx=Load())])), Assert(test=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='all', ctx=Load()), args=[Compare(left=Subscript(value=Attribute(value=Name(id='d', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='segments', ctx=Load()), Name(id='generated_c', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), ops=[Eq()], comparators=[Subscript(value=Attribute(value=Name(id='RESULT', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='segments', ctx=Load()), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())])], keywords=[]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='true_params'), Tuple(elts=[List(elts=[Constant(value='minute_in_hour_number')], ctx=Load()), List(elts=[Constant(value='fifteen_minutes_in_hour_number')], ctx=Load()), List(elts=[Constant(value='hour_number')], ctx=Load()), List(elts=[Constant(value='half_hour_number')], ctx=Load()), List(elts=[Constant(value='half_day_number')], ctx=Load()), List(elts=[Constant(value='one_third_day_number')], ctx=Load()), List(elts=[Constant(value='minute_in_hour_number'), Constant(value='fifteen_minutes_in_hour_number'), Constant(value='hour_number'), Constant(value='half_hour_number'), Constant(value='half_day_number'), Constant(value='one_third_day_number')], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='train_df', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='°GeneraϽte dataset țw¸ithout daƺteflags')), Assign(targets=[Name(id='DATAFRAMES', ctx=Store())], value=ListComp(elt=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp')], values=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[Constant(value='2020-06-01'), Constant(value='2021-06-01')], keywords=[keyword(arg='freq', value=Constant(value='5 min'))])])], keywords=[]), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='rangebqhZ', ctx=Load()), args=[Constant(value=5)], keywords=[]), ifs=[], is_async=0)])), For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='rangebqhZ', ctx=Load()), args=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='DATAFRAMES', ctx=Load())], keywords=[])], keywords=[]), body=[Assign(targets=[Name(id='df', ctx=Store())], value=Subscript(value=Name(id='DATAFRAMES', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Load())), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=JoinedStr(values=[Constant(value='segment_'), FormattedValue(value=Name(id='i', ctx=Load()), conversion=-1)])), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='target'), ctx=Store())], value=Constant(value=2))], orelse=[]), Assign(targets=[Name(id='RESULT', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[Name(id='DATAFRAMES', ctx=Load())], keywords=[keyword(arg='ignore_index', value=Constant(value=True))])), Assign(targets=[Name(id='RESULT', ctx=Store())], value=Call(func=Attribute(value=Name(id='RESULT', ctx=Load()), attr='pivot', ctx=Load()), args=[], keywords=[keyword(arg='index', value=Constant(value='timestamp')), keyword(arg='columns', value=Constant(value='segment'))])), Assign(targets=[Name(id='RESULT', ctx=Store())], value=Call(func=Attribute(value=Name(id='RESULT', ctx=Load()), attr='reorder_levels', ctx=Load()), args=[List(elts=[Constant(value=1), Constant(value=0)], ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='RESULT', ctx=Store())], value=Call(func=Attribute(value=Name(id='RESULT', ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Attribute(value=Attribute(value=Name(id='RESULT', ctx=Load()), attr='columns', ctx=Load()), attr='names', ctx=Store())], value=List(elts=[Constant(value='segment'), Constant(value='feature')], ctx=Load())), Return(value=Name(id='RESULT', ctx=Load()))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='test_interface_incorrect_args', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Name(id='TimeFlagsTransform', ctx=Load()), args=[], keywords=[keyword(arg='minute_in_hour_number', value=Constant(value=False)), keyword(arg='fifteen_minutes_in_hour_number', value=Constant(value=False)), keyword(arg='half_hour_number', value=Constant(value=False)), keyword(arg='hour_number', value=Constant(value=False)), keyword(arg='half_day_number', value=Constant(value=False)), keyword(arg='one_third_day_number', value=Constant(value=False))]))])], decorator_list=[]), FunctionDef(name='test_interface_out_column', args=arguments(posonlyargs=[], args=[arg(arg='TRUE_PARAMS', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='s', ctx=Load()), ctx=Load())), arg(arg='train_df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Test that transform generates correct coluŨmn names usÞing out_cońlumn parameter.')), Assign(targets=[Name(id='init_params', ctx=Store())], value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='INIT_PARAMS_TEMPLATE', ctx=Load())], keywords=[])), Assign(targets=[Name(id='segments', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='train_df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='out_column', ctx=Store())], value=Constant(value='timeflag')), For(target=Name(id='ke', ctx=Store()), iter=Name(id='TRUE_PARAMS', ctx=Load()), body=[Assign(targets=[Subscript(value=Name(id='init_params', ctx=Load()), slice=Name(id='ke', ctx=Load()), ctx=Store())], value=Constant(value=True))], orelse=[]), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='TimeFlagsTransform', ctx=Load()), args=[], keywords=[keyword(value=Name(id='init_params', ctx=Load())), keyword(arg='out_column', value=Name(id='out_column', ctx=Load()))])), Assign(targets=[Name(id='RESULT', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Call(func=Attribute(value=Name(id='train_df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[]))])), Assert(test=Compare(left=Call(func=Name(id='sorted', ctx=Load()), args=[Attribute(value=Attribute(value=Name(id='RESULT', ctx=Load()), attr='columns', ctx=Load()), attr='names', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[List(elts=[Constant(value='feature'), Constant(value='segment')], ctx=Load())])), Assert(test=Compare(left=Call(func=Name(id='sorted', ctx=Load()), args=[Name(id='segments', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='RESULT', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[])], keywords=[])])), Assign(targets=[Name(id='TRUE_PARAMS', ctx=Store())], value=ListComp(elt=JoinedStr(values=[FormattedValue(value=Name(id='out_column', ctx=Load()), conversion=-1), Constant(value='_'), FormattedValue(value=Name(id='param', ctx=Load()), conversion=-1)]), generators=[comprehension(target=Name(id='param', ctx=Store()), iter=Name(id='TRUE_PARAMS', ctx=Load()), ifs=[], is_async=0)])), For(target=Name(id='seg', ctx=Store()), iter=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='RESULT', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value=0)], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Name(id='tmp_df', ctx=Store())], value=Subscript(value=Name(id='RESULT', ctx=Load()), slice=Name(id='seg', ctx=Load()), ctx=Load())), Assert(test=Compare(left=Call(func=Name(id='sorted', ctx=Load()), args=[Attribute(value=Name(id='tmp_df', ctx=Load()), attr='columns', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='sorted', ctx=Load()), args=[BinOp(left=Name(id='TRUE_PARAMS', ctx=Load()), op=Add(), right=List(elts=[Constant(value='target')], ctx=Load()))], keywords=[])])), For(target=Name(id='param', ctx=Store()), iter=Name(id='TRUE_PARAMS', ctx=Load()), body=[Assert(test=Compare(left=Attribute(value=Subscript(value=Name(id='tmp_df', ctx=Load()), slice=Name(id='param', ctx=Load()), ctx=Load()), attr='dtype', ctx=Load()), ops=[Eq()], comparators=[Constant(value='category')]))], orelse=[])], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='true_params'), Tuple(elts=[List(elts=[Constant(value='minute_in_hour_number')], ctx=Load()), List(elts=[Constant(value='fifteen_minutes_in_hour_number')], ctx=Load()), List(elts=[Constant(value='hour_number')], ctx=Load()), List(elts=[Constant(value='half_hour_number')], ctx=Load()), List(elts=[Constant(value='half_day_number')], ctx=Load()), List(elts=[Constant(value='one_third_day_number')], ctx=Load()), List(elts=[Constant(value='minute_in_hour_number'), Constant(value='fifteen_minutes_in_hour_number'), Constant(value='hour_number'), Constant(value='half_hour_number'), Constant(value='half_day_number'), Constant(value='one_third_day_number')], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='dateflags_true_df', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Gȼenerate dataąset for TiʋmeFlags featu$ϣre.λ\nO\nRe¸turn\x8ds\n-------\ndĈaṭasetʪ with ˢtimestamp coͥlumn anͥd ĝcoɛ\x89lumnsö ϫtr˷ue_minutveη_Ŏinϗ_hour_nuɻĥmber, trɧue_fift%ee̸Ən_minutesƿ_in_hoÓNÌurƫ_nuƢJmber,\nt\x8arue_halfß̴_hƤouØr_\x8enumber, ƭtrueM_hoȟ¯uƇr_nuɊmber, trueā_half_όÁday_numϓǊber,Ø tƏrue_oneŁ_third_day_ĢΒnumύber that c̱ontaȆin\ntƨrue\u03a2 answerϮs for cor»¡respoǉǂnding feĩatures')), Assign(targets=[Name(id='DATAFRAMES', ctx=Store())], value=ListComp(elt=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp')], values=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[Constant(value='2020-06-01'), Constant(value='2021-06-01')], keywords=[keyword(arg='freq', value=Constant(value='5 min'))])])], keywords=[]), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='rangebqhZ', ctx=Load()), args=[Constant(value=5)], keywords=[]), ifs=[], is_async=0)])), Assign(targets=[Name(id='out_column', ctx=Store())], value=Constant(value='timeflag')), For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='rangebqhZ', ctx=Load()), args=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='DATAFRAMES', ctx=Load())], keywords=[])], keywords=[]), body=[Assign(targets=[Name(id='df', ctx=Store())], value=Subscript(value=Name(id='DATAFRAMES', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Load())), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=JoinedStr(values=[FormattedValue(value=Name(id='out_column', ctx=Load()), conversion=-1), Constant(value='_minute_in_hour_number')]), ctx=Store())], value=Attribute(value=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='timestamp'), ctx=Load()), attr='dt', ctx=Load()), attr='minute', ctx=Load())), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=JoinedStr(values=[FormattedValue(value=Name(id='out_column', ctx=Load()), conversion=-1), Constant(value='_fifteen_minutes_in_hour_number')]), ctx=Store())], value=BinOp(left=Subscript(value=Name(id='df', ctx=Load()), slice=JoinedStr(values=[FormattedValue(value=Name(id='out_column', ctx=Load()), conversion=-1), Constant(value='_minute_in_hour_number')]), ctx=Load()), op=FloorDiv(), right=Constant(value=15))), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=JoinedStr(values=[FormattedValue(value=Name(id='out_column', ctx=Load()), conversion=-1), Constant(value='_half_hour_number')]), ctx=Store())], value=BinOp(left=Subscript(value=Name(id='df', ctx=Load()), slice=JoinedStr(values=[FormattedValue(value=Name(id='out_column', ctx=Load()), conversion=-1), Constant(value='_minute_in_hour_number')]), ctx=Load()), op=FloorDiv(), right=Constant(value=30))), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=JoinedStr(values=[FormattedValue(value=Name(id='out_column', ctx=Load()), conversion=-1), Constant(value='_hour_number')]), ctx=Store())], value=Attribute(value=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='timestamp'), ctx=Load()), attr='dt', ctx=Load()), attr='hour', ctx=Load())), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=JoinedStr(values=[FormattedValue(value=Name(id='out_column', ctx=Load()), conversion=-1), Constant(value='_half_day_number')]), ctx=Store())], value=BinOp(left=Subscript(value=Name(id='df', ctx=Load()), slice=JoinedStr(values=[FormattedValue(value=Name(id='out_column', ctx=Load()), conversion=-1), Constant(value='_hour_number')]), ctx=Load()), op=FloorDiv(), right=Constant(value=12))), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=JoinedStr(values=[FormattedValue(value=Name(id='out_column', ctx=Load()), conversion=-1), Constant(value='_one_third_day_number')]), ctx=Store())], value=BinOp(left=Subscript(value=Name(id='df', ctx=Load()), slice=JoinedStr(values=[FormattedValue(value=Name(id='out_column', ctx=Load()), conversion=-1), Constant(value='_hour_number')]), ctx=Load()), op=FloorDiv(), right=Constant(value=8))), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=JoinedStr(values=[Constant(value='segment_'), FormattedValue(value=Name(id='i', ctx=Load()), conversion=-1)])), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='target'), ctx=Store())], value=Constant(value=2))], orelse=[]), Assign(targets=[Name(id='RESULT', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[Name(id='DATAFRAMES', ctx=Load())], keywords=[keyword(arg='ignore_index', value=Constant(value=True))])), Assign(targets=[Name(id='RESULT', ctx=Store())], value=Call(func=Attribute(value=Name(id='RESULT', ctx=Load()), attr='pivot', ctx=Load()), args=[], keywords=[keyword(arg='index', value=Constant(value='timestamp')), keyword(arg='columns', value=Constant(value='segment'))])), Assign(targets=[Name(id='RESULT', ctx=Store())], value=Call(func=Attribute(value=Name(id='RESULT', ctx=Load()), attr='reorder_levels', ctx=Load()), args=[List(elts=[Constant(value=1), Constant(value=0)], ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='RESULT', ctx=Store())], value=Call(func=Attribute(value=Name(id='RESULT', ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Attribute(value=Attribute(value=Name(id='RESULT', ctx=Load()), attr='columns', ctx=Load()), attr='names', ctx=Store())], value=List(elts=[Constant(value='segment'), Constant(value='feature')], ctx=Load())), Return(value=Name(id='RESULT', ctx=Load()))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='test_feature__values', args=arguments(posonlyargs=[], args=[arg(arg='TRUE_PARAMS', annotation=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='s', ctx=Load()), Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='bool', ctx=Load()), Subscript(value=Name(id='Tuple', ctx=Load()), slice=Tuple(elts=[Name(id='INT', ctx=Load()), Name(id='INT', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='train_df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='dateflags_true_df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='init_params', ctx=Store())], value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='INIT_PARAMS_TEMPLATE', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='init_params', ctx=Load()), attr='update', ctx=Load()), args=[Name(id='TRUE_PARAMS', ctx=Load())], keywords=[])), Assign(targets=[Name(id='out_column', ctx=Store())], value=Constant(value='timeflag')), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='TimeFlagsTransform', ctx=Load()), args=[], keywords=[keyword(value=Name(id='init_params', ctx=Load())), keyword(arg='out_column', value=Name(id='out_column', ctx=Load()))])), Assign(targets=[Name(id='RESULT', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Call(func=Attribute(value=Name(id='train_df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[]))])), Assign(targets=[Name(id='segments_true', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='dateflags_true_df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='segment', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='RESULT', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='sorted', ctx=Load()), args=[Name(id='segment', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='sorted', ctx=Load()), args=[Name(id='segments_true', ctx=Load())], keywords=[])])), Assign(targets=[Name(id='TRUE_PARAMS', ctx=Store())], value=ListComp(elt=JoinedStr(values=[FormattedValue(value=Name(id='out_column', ctx=Load()), conversion=-1), Constant(value='_'), FormattedValue(value=Name(id='param', ctx=Load()), conversion=-1)]), generators=[comprehension(target=Name(id='param', ctx=Store()), iter=Call(func=Attribute(value=Name(id='TRUE_PARAMS', ctx=Load()), attr='keys', ctx=Load()), args=[], keywords=[]), ifs=[], is_async=0)])), For(target=Name(id='seg', ctx=Store()), iter=Name(id='segment', ctx=Load()), body=[Assign(targets=[Name(id='segment_true', ctx=Store())], value=Subscript(value=Name(id='dateflags_true_df', ctx=Load()), slice=Name(id='seg', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='true__df', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='segment_true', ctx=Load()), slice=BinOp(left=Name(id='TRUE_PARAMS', ctx=Load()), op=Add(), right=List(elts=[Constant(value='target')], ctx=Load())), ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='RESULT', ctx=Load()), slice=Name(id='seg', ctx=Load()), ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assert(test=Call(func=Attribute(value=Call(func=Attribute(value=Compare(left=Name(id='true__df', ctx=Load()), ops=[Eq()], comparators=[Name(id='result_df', ctx=Load())]), attr='all', ctx=Load()), args=[], keywords=[]), attr='all', ctx=Load()), args=[], keywords=[]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='true_params'), Tuple(elts=[Dict(keys=[Constant(value='minute_in_hour_number')], values=[Constant(value=True)]), Dict(keys=[Constant(value='fifteen_minutes_in_hour_number')], values=[Constant(value=True)]), Dict(keys=[Constant(value='hour_number')], values=[Constant(value=True)]), Dict(keys=[Constant(value='half_hour_number')], values=[Constant(value=True)]), Dict(keys=[Constant(value='half_day_number')], values=[Constant(value=True)]), Dict(keys=[Constant(value='one_third_day_number')], values=[Constant(value=True)])], ctx=Load())], keywords=[])])], type_ignores=[])