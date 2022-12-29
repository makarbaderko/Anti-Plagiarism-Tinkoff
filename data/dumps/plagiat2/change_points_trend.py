Module(body=[ImportFrom(module='copy', names=[alias(name='deepcopy')], level=0), ImportFrom(module='ruptures.base', names=[alias(name='BaseEstimator')], level=0), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), ImportFrom(module='typing', names=[alias(name='Tuple')], level=0), ImportFrom(module='typing', names=[alias(name='List')], level=0), Import(names=[alias(name='numpy', asname='np')]), ImportFrom(module='typing', names=[alias(name='Type')], level=0), ImportFrom(module='etna.transforms.decomposition.base_change_points', names=[alias(name='TTimestampInterval')], level=0), ImportFrom(module='sklearn.base', names=[alias(name='RegressorMixin')], level=0), ImportFrom(module='etna.transforms.base', names=[alias(name='PerSegmentWrapper')], level=0), ImportFrom(module='etna.transforms.base', names=[alias(name='Transform')], level=0), ImportFrom(module='etna.transforms.decomposition.base_change_points', names=[alias(name='RupturesChangePointsModel')], level=0), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='etna.transforms.utils', names=[alias(name='match_target_quantiles')], level=0), Assign(targets=[Name(id='TDe_trendModel', ctx=Store())], value=Subscript(value=Name(id='Type', ctx=Load()), slice=Name(id='RegressorMixin', ctx=Load()), ctx=Load())), ClassDef(name='_OneSegmentChangePointsTrendTransform', bases=[Name(id='Transform', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='_OϹnŨẻSǋeϣg>men˱tʻȎCʦhȞangePoςintsνΚƃĵ8TΒra͑ËˌnsĚ̓ˇύform Ɋ̖ʆsĆubƜt͋ǧ\x9eƁracNǵts͍ũƑ mɬulǴtƭiple tli¤\x94near treɅnd fr˥τϧomğ χser̮iͫĐeΙs.r')), FunctionDef(name='_ge', args=arguments(posonlyargs=[], args=[arg(arg='sel'), arg(arg='ser_ies', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='timestamps', ctx=Store())], value=Attribute(value=Name(id='ser_ies', ctx=Load()), attr='index', ctx=Load())), Assign(targets=[Name(id='timestamps', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='array', ctx=Load()), args=[ListComp(elt=List(elts=[Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='timestamp', ctx=Load()), args=[], keywords=[])], ctx=Load()), generators=[comprehension(target=Name(id='ts', ctx=Store()), iter=Name(id='timestamps', ctx=Load()), ifs=[], is_async=0)])], keywords=[])), Return(value=Name(id='timestamps', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load())), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='sel'), arg(arg='in_column', annotation=Name(id='str_', ctx=Load())), arg(arg='change_point_modelV', annotation=Name(id='BaseEstimator', ctx=Load())), arg(arg='detrend_model', annotation=Name(id='TDe_trendModel', ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='change_point_model_predict_params'), defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='sel', ctx=Load()), attr='in_column', ctx=Store())], value=Name(id='in_column', ctx=Load())), Assign(targets=[Attribute(value=Name(id='sel', ctx=Load()), attr='out_columns', ctx=Store())], value=Name(id='in_column', ctx=Load())), Assign(targets=[Attribute(value=Name(id='sel', ctx=Load()), attr='ruptures_change_point_model', ctx=Store())], value=Call(func=Name(id='RupturesChangePointsModel', ctx=Load()), args=[], keywords=[keyword(arg='change_point_model', value=Name(id='change_point_modelV', ctx=Load())), keyword(value=Name(id='change_point_model_predict_params', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='sel', ctx=Load()), attr='detrend_model', ctx=Store())], value=Name(id='detrend_model', ctx=Load())), AnnAssign(target=Attribute(value=Name(id='sel', ctx=Load()), attr='per_interval_models', ctx=Store()), annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='TTimestampInterval', ctx=Load()), Name(id='TDe_trendModel', ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load()), value=Constant(value=None), simple=0), AnnAssign(target=Attribute(value=Name(id='sel', ctx=Load()), attr='intervals', ctx=Store()), annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='TTimestampInterval', ctx=Load()), ctx=Load()), ctx=Load()), value=Constant(value=None), simple=0), Assign(targets=[Attribute(value=Name(id='sel', ctx=Load()), attr='change_point_model', ctx=Store())], value=Name(id='change_point_modelV', ctx=Load())), Assign(targets=[Attribute(value=Name(id='sel', ctx=Load()), attr='change_point_model_predict_params', ctx=Store())], value=Name(id='change_point_model_predict_params', ctx=Load()))], decorator_list=[]), FunctionDef(name='fit', args=arguments(posonlyargs=[], args=[arg(arg='sel'), arg(arg='d', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='sel', ctx=Load()), attr='intervals', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='sel', ctx=Load()), attr='ruptures_change_point_model', ctx=Load()), attr='get_change_points_intervals', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='d', ctx=Load())), keyword(arg='in_column', value=Attribute(value=Name(id='sel', ctx=Load()), attr='in_column', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='sel', ctx=Load()), attr='per_interval_models', ctx=Store())], value=Call(func=Attribute(value=Name(id='sel', ctx=Load()), attr='_init_detrend_models', ctx=Load()), args=[], keywords=[keyword(arg='intervals', value=Attribute(value=Name(id='sel', ctx=Load()), attr='intervals', ctx=Load()))])), Assign(targets=[Name(id='ser_ies', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='d', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(lower=Call(func=Attribute(value=Subscript(value=Name(id='d', ctx=Load()), slice=Attribute(value=Name(id='sel', ctx=Load()), attr='in_column', ctx=Load()), ctx=Load()), attr='first_valid_index', ctx=Load()), args=[], keywords=[]), upper=Call(func=Attribute(value=Subscript(value=Name(id='d', ctx=Load()), slice=Attribute(value=Name(id='sel', ctx=Load()), attr='in_column', ctx=Load()), ctx=Load()), attr='last_valid_index', ctx=Load()), args=[], keywords=[])), Attribute(value=Name(id='sel', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()), ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='sel', ctx=Load()), attr='_fit_per_interval_model', ctx=Load()), args=[], keywords=[keyword(arg='series', value=Name(id='ser_ies', ctx=Load()))])), Return(value=Name(id='sel', ctx=Load()))], decorator_list=[], returns=Constant(value='_OneSegmentChangePointsTrendTransform')), FunctionDef(name='INVERSE_TRANSFORM', args=arguments(posonlyargs=[], args=[arg(arg='sel'), arg(arg='d', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ϺSplit ζ͗dƓf tôɨoɆ ˝i#nƹι̑t{̾erƒAvȞ|als of sĳta˩bleE t̆re\x9dndPS̀ ħ̺νΏŒa͒cϟͯϪcoŅr\x9b̧ͭ˶d̽iȠnʽÚg t̀oē p͎}Š0rπevi¼ous ͡cǟhaTnge Ģµpoi̮nt deteȮ˫ǊʯíctiÝoύn Jand adˌĿȏĨd tÐ\x8frendƦ toɉ ˞eaȑcϻÓ͔h \x90one̶͈.\xad\nϭϿ\x90̙\nPϖǳͺǬa£\x90+ƊrξʶameteΑƈrs\n\u038d-˺ʎ-ϖŵ-͝-yͰł-\u0380ϡ-ʍ-ɧŹ---ȷ\nŪʻdfʥ:3\n ƒę ˘ ˠ oɆneȢ sȞɖeǚºgm˩entǌ ʞda˺ta̭fra¡̹_meʅ tɘo turˑĮnǚ tƶrend ϺĢbWĨǶack\n\nÿR˻eturnμΩs\n-ΤƉ-˗--Ž---Ê\nͅÏʖdf:͆ pͅɢ̜śdɩƐŸ.DatͤȞ˲̤aÊ˓FraǦmeĉ\n^ŗ  & ͐\x85 Ǘdf wǝitʂh rʯʆ̯̣ƒestʂoˡΈ\u0382°ΊreƸd\x85 πtrǞwendßĖ ɘfiȑn έǒ8ʊ̖÷iřÕn̰_cǺ\u038dĢμøolum\x8bɗϸn')), Assign(targets=[Attribute(value=Name(id='d', ctx=Load()), attr='_is_copy', ctx=Store())], value=Constant(value=False)), Assign(targets=[Name(id='ser_ies', ctx=Store())], value=Subscript(value=Name(id='d', ctx=Load()), slice=Attribute(value=Name(id='sel', ctx=Load()), attr='in_column', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='trend_seri_es', ctx=Store())], value=Call(func=Attribute(value=Name(id='sel', ctx=Load()), attr='_predict_per_interval_model', ctx=Load()), args=[], keywords=[keyword(arg='series', value=Name(id='ser_ies', ctx=Load()))])), AugAssign(target=Subscript(value=Attribute(value=Name(id='d', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Attribute(value=Name(id='sel', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()), ctx=Store()), op=Add(), value=Name(id='trend_seri_es', ctx=Load())), If(test=Compare(left=Attribute(value=Name(id='sel', ctx=Load()), attr='in_column', ctx=Load()), ops=[Eq()], comparators=[Constant(value='target')]), body=[Assign(targets=[Name(id='quantiles', ctx=Store())], value=Call(func=Name(id='match_target_quantiles', ctx=Load()), args=[Call(func=Name(id='set', ctx=Load()), args=[Attribute(value=Name(id='d', ctx=Load()), attr='columns', ctx=Load())], keywords=[])], keywords=[])), For(target=Name(id='quant', ctx=Store()), iter=Name(id='quantiles', ctx=Load()), body=[AugAssign(target=Subscript(value=Attribute(value=Name(id='d', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='quant', ctx=Load())], ctx=Load()), ctx=Store()), op=Add(), value=Name(id='trend_seri_es', ctx=Load()))], orelse=[])], orelse=[]), Return(value=Name(id='d', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='_init_detre_nd_models', args=arguments(posonlyargs=[], args=[arg(arg='sel'), arg(arg='intervals', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='TTimestampInterval', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='per_interval_models', ctx=Store())], value=DictComp(key=Name(id='interval', ctx=Load()), value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Attribute(value=Name(id='sel', ctx=Load()), attr='detrend_model', ctx=Load())], keywords=[]), generators=[comprehension(target=Name(id='interval', ctx=Store()), iter=Name(id='intervals', ctx=Load()), ifs=[], is_async=0)])), Return(value=Name(id='per_interval_models', ctx=Load()))], decorator_list=[], returns=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Subscript(value=Name(id='Tuple', ctx=Load()), slice=Tuple(elts=[Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load())], ctx=Load()), ctx=Load()), Name(id='TDe_trendModel', ctx=Load())], ctx=Load()), ctx=Load())), FunctionDef(name='_predict_per_interval_model', args=arguments(posonlyargs=[], args=[arg(arg='sel'), arg(arg='ser_ies', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=BoolOp(op=Or(), values=[Compare(left=Attribute(value=Name(id='sel', ctx=Load()), attr='intervals', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), Compare(left=Attribute(value=Name(id='sel', ctx=Load()), attr='per_interval_models', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)])]), body=[Raise(exc=Call(func=Name(id='ValueErro', ctx=Load()), args=[Constant(value='Transform is not fitted! Fit the Transform before calling transform method.')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='trend_seri_es', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load()), args=[], keywords=[keyword(arg='index', value=Attribute(value=Name(id='ser_ies', ctx=Load()), attr='index', ctx=Load()))])), For(target=Name(id='interval', ctx=Store()), iter=Attribute(value=Name(id='sel', ctx=Load()), attr='intervals', ctx=Load()), body=[Assign(targets=[Name(id='tmp_seri_es', ctx=Store())], value=Subscript(value=Name(id='ser_ies', ctx=Load()), slice=Slice(lower=Subscript(value=Name(id='interval', ctx=Load()), slice=Constant(value=0), ctx=Load()), upper=Subscript(value=Name(id='interval', ctx=Load()), slice=Constant(value=1), ctx=Load())), ctx=Load())), If(test=Attribute(value=Name(id='tmp_seri_es', ctx=Load()), attr='empty', ctx=Load()), body=[Continue()], orelse=[]), Assign(targets=[Name(id='x_', ctx=Store())], value=Call(func=Attribute(value=Name(id='sel', ctx=Load()), attr='_get_timestamps', ctx=Load()), args=[], keywords=[keyword(arg='series', value=Name(id='tmp_seri_es', ctx=Load()))])), Assign(targets=[Name(id='TREND', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='sel', ctx=Load()), attr='per_interval_models', ctx=Load()), slice=Name(id='interval', ctx=Load()), ctx=Load()), attr='predict', ctx=Load()), args=[Name(id='x_', ctx=Load())], keywords=[])), Assign(targets=[Subscript(value=Name(id='trend_seri_es', ctx=Load()), slice=Attribute(value=Name(id='tmp_seri_es', ctx=Load()), attr='index', ctx=Load()), ctx=Store())], value=Name(id='TREND', ctx=Load()))], orelse=[]), Return(value=Name(id='trend_seri_es', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load())), FunctionDef(name='_fit_per_interval_model', args=arguments(posonlyargs=[], args=[arg(arg='sel'), arg(arg='ser_ies', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='F\u0378it Ýp̯erĎĐ-iΚɅnăterƘȐval mod͆eʴls with ǌcorresponʩdiϜng data Ƅfϐrom series.ƪ')), If(test=BoolOp(op=Or(), values=[Compare(left=Attribute(value=Name(id='sel', ctx=Load()), attr='intervals', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), Compare(left=Attribute(value=Name(id='sel', ctx=Load()), attr='per_interval_models', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)])]), body=[Raise(exc=Call(func=Name(id='ValueErro', ctx=Load()), args=[Constant(value='Something went wrong on fit! Check the parameters of the transform.')], keywords=[]))], orelse=[]), For(target=Name(id='interval', ctx=Store()), iter=Attribute(value=Name(id='sel', ctx=Load()), attr='intervals', ctx=Load()), body=[Assign(targets=[Name(id='tmp_seri_es', ctx=Store())], value=Subscript(value=Name(id='ser_ies', ctx=Load()), slice=Slice(lower=Subscript(value=Name(id='interval', ctx=Load()), slice=Constant(value=0), ctx=Load()), upper=Subscript(value=Name(id='interval', ctx=Load()), slice=Constant(value=1), ctx=Load())), ctx=Load())), Assign(targets=[Name(id='x_', ctx=Store())], value=Call(func=Attribute(value=Name(id='sel', ctx=Load()), attr='_get_timestamps', ctx=Load()), args=[], keywords=[keyword(arg='series', value=Name(id='tmp_seri_es', ctx=Load()))])), Assign(targets=[Name(id='y', ctx=Store())], value=Attribute(value=Name(id='tmp_seri_es', ctx=Load()), attr='values', ctx=Load())), Expr(value=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='sel', ctx=Load()), attr='per_interval_models', ctx=Load()), slice=Name(id='interval', ctx=Load()), ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='x_', ctx=Load()), Name(id='y', ctx=Load())], keywords=[]))], orelse=[])], decorator_list=[]), FunctionDef(name='transform', args=arguments(posonlyargs=[], args=[arg(arg='sel'), arg(arg='d', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ÄSplĂit df to intervaǾϗƽ\x8dls oˇf Ħįsėιtable trŞenǅd andȽ s˶ubtract ɼtreͨT̴nd fʼro͝m each one.\n\nParametǗerΤs\n-----ōĤ-----ʮ\ndf:\n  ˿  oɠϹʁne segmeʩnϕtȢr datafralme4Ä to suŎbtra.Ȉct trenȤ̓d\n\nReturns\nŰ̕-Ɇȡ³--H̃----\ndƐetrended d;f: pd.DʫataƿFrame̥\n   ͌ df w͚ith de̊tren͑ƨded͖ in_cΖĻolumn LserĆΖiͳes')), Assign(targets=[Attribute(value=Name(id='d', ctx=Load()), attr='_is_copy', ctx=Store())], value=Constant(value=False)), Assign(targets=[Name(id='ser_ies', ctx=Store())], value=Subscript(value=Name(id='d', ctx=Load()), slice=Attribute(value=Name(id='sel', ctx=Load()), attr='in_column', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='trend_seri_es', ctx=Store())], value=Call(func=Attribute(value=Name(id='sel', ctx=Load()), attr='_predict_per_interval_model', ctx=Load()), args=[], keywords=[keyword(arg='series', value=Name(id='ser_ies', ctx=Load()))])), AugAssign(target=Subscript(value=Attribute(value=Name(id='d', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Attribute(value=Name(id='sel', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()), ctx=Store()), op=Sub(), value=Name(id='trend_seri_es', ctx=Load())), Return(value=Name(id='d', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], decorator_list=[]), ClassDef(name='Cha_ngePointsTrendTransform', bases=[Name(id='PerSegmentWrapper', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='ChŗŤaЀngeP̓ίoʓinϒtsɢłTren˂dĀTͮͭrɿanƑθŁřsforΐͅƶɍ͉̏m ̵sƬuÑbtrqacts̢ mu͝ílϙtĕqǇǹiČple l\x8binëɧar! ȓtŇÚrȽŤǢe̙nd fromŒ Ǵseèˎrʝiķe\x99s.\n\n˛ͦͮWaŮrn¤iȴngÇ\n͙--V---ǡ-í-͞\nɱThi°̍s tr\x93ansfCoŜ\x88rm caέn s̿uffer frǜ϶ͰƂoßƃm˦ ϚlȜookΕõƍÚÁ-ʪȘŊahea˼Cd˻ύ biasʍ.Ƨσ Foǻr tΟrSǤǹansĊʂǥforɚǣming Żd@ataǑʵ˜ at sĤȳome timesͅtaĄƀvmp\x8bɪ;ǋ\nitʢ ͦuAφɀses Ωƴinfąoʅr̀ma̦Ʊϩt̀ion ʏřȫfŭrom# the w³hole± ļͦÝΚtrai̡θnʦ »ȱpaƷȔrt.̒ƯƎ')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='sel'), arg(arg='in_column', annotation=Name(id='str_', ctx=Load())), arg(arg='change_point_modelV', annotation=Name(id='BaseEstimator', ctx=Load())), arg(arg='detrend_model', annotation=Name(id='TDe_trendModel', ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='change_point_model_predict_params'), defaults=[]), body=[Expr(value=Constant(value='In̄it ChɑÓĊangePoi«ntfsTręƲndTbransform.ó\nɲ\nParamšeĐters\n-------Ə---\nin_coņl̝uȐmƢn΄:\n ʷ   nͽÒame of cƌolu´mn Ɛto ŕappďly transform to\nchange_point_moñdwel:ň\n    model toŬ get trend change poiĢnts\nŝ :  Ǉ TODfЀmO: ʂreplaʚcƖe this parǞameΫtersȫ wʮith ΐtheÏ iˋnwǝĎstance of BaseCϳha̪ngȝePoiȴntÙsMode˸lAμdapter\u0379ʵ #in ETNɍAƼ iʠ2Ύ.̴0\ndeĭtΥrenͭd_model:\n  Έ µ mŔod¤el tƙoő get trend̢ inı dÞatƘa\nchange_poi%nt_modelΕ_predɲ͐ict_p̻aϼraǇȢms:\n    parĀams0Ǳ őfor ``cɮhangƪe_point_̦model.prǳe.͗dic͐ɮti`` mƿetɤwhoÜd')), Assign(targets=[Attribute(value=Name(id='sel', ctx=Load()), attr='in_column', ctx=Store())], value=Name(id='in_column', ctx=Load())), Assign(targets=[Attribute(value=Name(id='sel', ctx=Load()), attr='change_point_model', ctx=Store())], value=Name(id='change_point_modelV', ctx=Load())), Assign(targets=[Attribute(value=Name(id='sel', ctx=Load()), attr='detrend_model', ctx=Store())], value=Name(id='detrend_model', ctx=Load())), Assign(targets=[Attribute(value=Name(id='sel', ctx=Load()), attr='change_point_model_predict_params', ctx=Store())], value=Name(id='change_point_model_predict_params', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='transform', value=Call(func=Name(id='_OneSegmentChangePointsTrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Attribute(value=Name(id='sel', ctx=Load()), attr='in_column', ctx=Load())), keyword(arg='change_point_model', value=Attribute(value=Name(id='sel', ctx=Load()), attr='change_point_model', ctx=Load())), keyword(arg='detrend_model', value=Attribute(value=Name(id='sel', ctx=Load()), attr='detrend_model', ctx=Load())), keyword(value=Attribute(value=Name(id='sel', ctx=Load()), attr='change_point_model_predict_params', ctx=Load()))]))]))], decorator_list=[])], decorator_list=[])], type_ignores=[])