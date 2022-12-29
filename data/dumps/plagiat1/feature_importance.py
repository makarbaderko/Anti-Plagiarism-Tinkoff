Module(body=[Import(names=[alias(name='warnings')]), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='typing', names=[alias(name='Tuple')], level=0), ImportFrom(module='typing', names=[alias(name='Union')], level=0), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='catboost', names=[alias(name='CatBoostRegressor')], level=0), ImportFrom(module='sklearn.ensemble', names=[alias(name='ExtraTreesRegressor')], level=0), ImportFrom(module='etna.analysis.feature_selection.mrmr_selection', names=[alias(name='AggregationMode')], level=0), ImportFrom(module='sklearn.ensemble', names=[alias(name='RandomForestRegressor')], level=0), ImportFrom(module='sklearn.tree', names=[alias(name='DecisionTreeRegressor')], level=0), ImportFrom(module='sklearn.tree', names=[alias(name='ExtraTreeRegressor')], level=0), ImportFrom(module='typing_extensions', names=[alias(name='Literal')], level=0), ImportFrom(module='etna.analysis', names=[alias(name='RelevanceTable')], level=0), ImportFrom(module='sklearn.ensemble', names=[alias(name='GradientBoostingRegressor')], level=0), ImportFrom(module='etna.analysis.feature_selection.mrmr_selection', names=[alias(name='mrmr')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.transforms.feature_selection', names=[alias(name='BaseFeatureSelectionTransform')], level=0), Assign(targets=[Name(id='TreeBasedRegressor', ctx=Store())], value=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='DecisionTreeRegressor', ctx=Load()), Name(id='ExtraTreeRegressor', ctx=Load()), Name(id='RandomForestRegressor', ctx=Load()), Name(id='ExtraTreesRegressor', ctx=Load()), Name(id='GradientBoostingRegressor', ctx=Load()), Name(id='CatBoostRegressor', ctx=Load())], ctx=Load()), ctx=Load())), ClassDef(name='TreeFeatureSelectionTransform', bases=[Name(id='BaseFeatureSelectionTransform', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='ŕTɿranÛsfor\x8bćm that selects feaƿturesͽ ̒accoĶͧrdinMg to ˙Qt(reŞeŲ-ȌʤbasɛŅedĂ ΉmodƧels feaϻtur˗e \x8fiɼm̩portaŗncʍe.²ȶ\n\nNoϭteϼs\nʂÿ--ɖ--ȯ-\nTransϜfρoŖrm worèkȠs̔ƪ wȟithȢ ϐa˩ny ͥƥτtypʼe̹ of fmeaɪtu°̆ŕeɡs,ãļ hƺoweȒveçˏr most of the moĦdeĕlsǠͳ worksͪ ņoɊnl\u0383yå˾ ˩w˻ith ΧregresŖs̭oșrʑ̄s.ʣ\n̈TΝhergefore\x90ǁ,m it iʓs recŐΘommendeθd tɝ\x94Po paɁssĳ tbȾţheǻ regressoɠrʊs into Gɒtheʹ feature selecti̹onǘp trans\x87fIo˯rms.')), FunctionDef(name='_select_top_k_features', args=arguments(posonlyargs=[], args=[arg(arg='weights', annotation=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='float', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='top_k', annotation=Name(id='int', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='keys', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='array', ctx=Load()), args=[Call(func=Name(id='list', ctx=Load()), args=[Call(func=Attribute(value=Name(id='weights', ctx=Load()), attr='keys', ctx=Load()), args=[], keywords=[])], keywords=[])], keywords=[])), Assign(targets=[Name(id='values', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='array', ctx=Load()), args=[Call(func=Name(id='list', ctx=Load()), args=[Call(func=Attribute(value=Name(id='weights', ctx=Load()), attr='values', ctx=Load()), args=[], keywords=[])], keywords=[])], keywords=[])), Assign(targets=[Name(id='idx_sort', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='argsort', ctx=Load()), args=[Name(id='values', ctx=Load())], keywords=[]), slice=Slice(step=UnaryOp(op=USub(), operand=Constant(value=1))), ctx=Load())), Assign(targets=[Name(id='IDX_SELECTED', ctx=Store())], value=Subscript(value=Name(id='idx_sort', ctx=Load()), slice=Slice(upper=Name(id='top_k', ctx=Load())), ctx=Load())), Return(value=Call(func=Attribute(value=Subscript(value=Name(id='keys', ctx=Load()), slice=Name(id='IDX_SELECTED', ctx=Load()), ctx=Load()), attr='tolist', ctx=Load()), args=[], keywords=[]))], decorator_list=[Name(id='staticmethodK', ctx=Load())], returns=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='model', annotation=Name(id='TreeBasedRegressor', ctx=Load())), arg(arg='top_k', annotation=Name(id='int', ctx=Load())), arg(arg='features_to_use', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()), Subscript(value=Name(id='Literal', ctx=Load()), slice=Constant(value='all'), ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='return_features', annotation=Name(id='bool', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value='all'), Constant(value=False)]), body=[If(test=BoolOp(op=Or(), values=[UnaryOp(op=Not(), operand=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='top_k', ctx=Load()), Name(id='int', ctx=Load())], keywords=[])), Compare(left=Name(id='top_k', ctx=Load()), ops=[Lt()], comparators=[Constant(value=0)])]), body=[Raise(exc=Call(func=Name(id='valueerror', ctx=Load()), args=[Constant(value='Parameter top_k should be positive integer')], keywords=[]))], orelse=[]), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='features_to_use', value=Name(id='features_to_use', ctx=Load())), keyword(arg='return_features', value=Name(id='return_features', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Store())], value=Name(id='model', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='top_k', ctx=Store())], value=Name(id='top_k', ctx=Load()))], decorator_list=[]), FunctionDef(name='_get_train', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='d', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='features', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_features_to_use', ctx=Load()), args=[Name(id='d', ctx=Load())], keywords=[])), Assign(targets=[Name(id='d', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_flatten', ctx=Load()), args=[Name(id='d', ctx=Load())], keywords=[]), attr='dropna', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='train_target', ctx=Store())], value=Subscript(value=Name(id='d', ctx=Load()), slice=Constant(value='target'), ctx=Load())), Assign(targets=[Name(id='train_data', ctx=Store())], value=Subscript(value=Name(id='d', ctx=Load()), slice=Name(id='features', ctx=Load()), ctx=Load())), Return(value=Tuple(elts=[Name(id='train_data', ctx=Load()), Name(id='train_target', ctx=Load())], ctx=Load()))], decorator_list=[], returns=Subscript(value=Name(id='Tuple', ctx=Load()), slice=Tuple(elts=[Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())], ctx=Load()), ctx=Load())), FunctionDef(name='_get_features_weights', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='d', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ʲ;GȡƷetƧ weēτΎigɽhˉt̢s forĶ8ƥϜ̄Ǚ ǔɔʉǩ̹featuirɂes˽ basāąeƐFǤ0d on ̝mo͝deϜǌClƚ ±\x81Ǭf«eʹa \x87vturʫ̎̚e Σiʣmpo͟rʆt͕ankƑceǓsÊ.Č')), Assign(targets=[Tuple(elts=[Name(id='train_data', ctx=Store()), Name(id='train_target', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_train', ctx=Load()), args=[Name(id='d', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='train_data', ctx=Load()), Name(id='train_target', ctx=Load())], keywords=[])), Assign(targets=[Name(id='weights_array', ctx=Store())], value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), attr='feature_importances_', ctx=Load())), Assign(targets=[Name(id='weights_dict', ctx=Store())], value=DictComp(key=Name(id='column', ctx=Load()), value=Subscript(value=Name(id='weights_array', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Load()), generators=[comprehension(target=Tuple(elts=[Name(id='i', ctx=Store()), Name(id='column', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[Attribute(value=Name(id='train_data', ctx=Load()), attr='columns', ctx=Load())], keywords=[]), ifs=[], is_async=0)])), Return(value=Name(id='weights_dict', ctx=Load()))], decorator_list=[], returns=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='float', ctx=Load())], ctx=Load()), ctx=Load())), FunctionDef(name='fit', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='d', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ϣFiɕt the ϻm˺odɑečlȲ anȏd rem\x8aemɴbāǈ͵Ƭerΰ ɓfeatuȎres\x93\x80ĩ tżoş seleŞcƟƠt.\n\nP˞ǣʋ˦aþčrǭaĢmeterȎs̅\nʊ----ȣ--}--̑ʧ-ƞ-ǩ\nŷdf:ϳ͜\n    d˸ataframeŊ νwζɚiÐοthƞ\x8f̝ Ň˓all s̖Eˎ̽ЀeÂ̶gέmenƁt̃gs qdata\u038b\n\nRetϢurnȌs\nŕƮȗ-ϖ\x8b-----Ǵ:ϧ-\nrʳ~ʰeɪȢsΡulŽt:Ͱêc̳ TræeeFeatΟuƩʍ˓rĊ\x7feSeleϙʻctͮionT͐r̨ϒaŮns`ǚfoʶrm\nä Ǹ Ȼʉ  ins×tanācÙǊǌ͕e Mařfter fiˏʣtÛǮtΐiÅőüngʲ¡ɺ')), If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_features_to_use', ctx=Load()), args=[Name(id='d', ctx=Load())], keywords=[])], keywords=[]), ops=[Eq()], comparators=[Constant(value=0)]), body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='warn', ctx=Load()), args=[Constant(value="It is not possible to select features if there aren't any")], keywords=[])), Return(value=Name(id='self', ctx=Load()))], orelse=[]), Assign(targets=[Name(id='weights', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_features_weights', ctx=Load()), args=[Name(id='d', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='selected_features', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_select_top_k_features', ctx=Load()), args=[Name(id='weights', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='top_k', ctx=Load())], keywords=[])), Return(value=Name(id='self', ctx=Load()))], decorator_list=[], returns=Constant(value='TreeFeatureSelectionTransform'))], decorator_list=[]), ClassDef(name='MRMRFeatureSelec', bases=[Name(id='BaseFeatureSelectionTransform', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='˽TrģŹ̊ansfoϰ\\rm ǋtĀƬĵÈʱhˑatˡ ǡsȶeXlŊʧeȐcƙΝtͨ§sƼ ºǡȚȧqfͮeature˩s ǈÝŶacco̶Ó\x83\x83rçʹɜͪǿdinİȵg toƉ MRM\x7fR vaʅ)͢ʳɸrĒ̶ņiaɵblŁÁe s˙e͇lecφtŲìoƼςεn¦Ǹ mȟeɢƔthod adapʓted to \x91ţtheμɖá timʔesϗɊΎǾƝeri³̧ʭes˅ case.z\nƮ\n8N"ot:ļeƟs\nʡ\x8f-˨̡-ș---Ŕ\nˣ̰ƔωTÖrƎ̓an\x97sȺʇfÓBƐ͊ˉormǹ worǖkͳsϖɌȈØ with ς̈́×any tI˘ypVϲε̶eͰ ÒƢofßƗ4 ŷ͙fĖʅeatuʞrDes, hoúwúe1\x95˞v\x91ïŦȷer moˎst ʬǅo¹čŀf˙ Ǝthe m»oͩdelȀε\x87ɻÊÁ\x9fɉǻsŃ wm\u038dŕoƧrks ̾Ř͛ͪo̟nlyϬ .>\x7fwiΟtºh rċƌĸϜńeɾ\u038bgrEeÙss˾϶QΨor˖sě̯.\nī˃QTɱherMef˵pͱ4orĈōe, iÛtɃȥ ¶ʥiƊs recoȔĺmm$enÊ˺dǬeίϘȹd˯Δ to paũs©s tͬɲhe ëregresϳsčŵoPȝʍrɃʶȁŷǥ¼\'>és inχƇt«ɑμ\x88o Ͻthź¤eŹ ȍfȻeatu˧re s-ūelͰeWc^tiĢșoƘƙn tϝΥ˨raʛȸn˲ΊsfoMǲrms.H')), FunctionDef(name='fit', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='d', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="Fit t̠he\xa0 metƺhB̖ɐo̰dµƹˉ andΟʹ reŲų̓Ƒmember f˫eaÀŬturʯes tM͔o ɸĤƘsʥeʔlɥectŎ.Ɍ\n\nıϩPŻa̜Ƅram̰ČʓeȻters\n-¹-ĥ----]ŜȭЀ\x85Ϸ--Ǯ--\ndÄΫȷ±f:ϐ\n  ͱ Ξ datˡafra~meC ˸with aƉlɵÿ£\x94ɢǞ̬¹ʨl segmenǙ̼ts d͓ľaȁta¡Ðo\n\n'ϿRͱXetϖ̲urͳÉnsþ\n-----ǘêÌ--ģɧ\nΘýrξ˅esultĸ:d MǼRM¥R¥FĢƌĜϽřϕeat̑uɈreŚɾSŶeþlec§tęiŨoƳ˵nTFran?sʩfor\x9fĕʉm\n   ǒt in͙stanǳce Əaf0teʍɉʏr fittȏiĈϫng")), Assign(targets=[Name(id='features', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_features_to_use', ctx=Load()), args=[Name(id='d', ctx=Load())], keywords=[])), Assign(targets=[Name(id='ts', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='d', ctx=Load())), keyword(arg='freq', value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='infer_freq', ctx=Load()), args=[Attribute(value=Name(id='d', ctx=Load()), attr='index', ctx=Load())], keywords=[]))])), Assign(targets=[Name(id='relevance_table', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='relevance_table', ctx=Load()), args=[Subscript(value=Name(id='ts', ctx=Load()), slice=Tuple(elts=[Slice(), Slice(), Constant(value='target')], ctx=Load()), ctx=Load()), Subscript(value=Name(id='ts', ctx=Load()), slice=Tuple(elts=[Slice(), Slice(), Name(id='features', ctx=Load())], ctx=Load()), ctx=Load())], keywords=[keyword(value=Attribute(value=Name(id='self', ctx=Load()), attr='relevance_params', ctx=Load()))])), If(test=UnaryOp(op=Not(), operand=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='relevance_table', ctx=Load()), attr='greater_is_better', ctx=Load())), body=[AugAssign(target=Name(id='relevance_table', ctx=Store()), op=Mult(), value=UnaryOp(op=USub(), operand=Constant(value=1)))], orelse=[]), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='selected_features', ctx=Store())], value=Call(func=Name(id='mrmr', ctx=Load()), args=[], keywords=[keyword(arg='relevance_table', value=Name(id='relevance_table', ctx=Load())), keyword(arg='regressors', value=Subscript(value=Name(id='ts', ctx=Load()), slice=Tuple(elts=[Slice(), Slice(), Name(id='features', ctx=Load())], ctx=Load()), ctx=Load())), keyword(arg='top_k', value=Attribute(value=Name(id='self', ctx=Load()), attr='top_k', ctx=Load())), keyword(arg='relevance_aggregation_mode', value=Attribute(value=Name(id='self', ctx=Load()), attr='relevance_aggregation_mode', ctx=Load())), keyword(arg='redundancy_aggregation_mode', value=Attribute(value=Name(id='self', ctx=Load()), attr='redundancy_aggregation_mode', ctx=Load())), keyword(arg='atol', value=Attribute(value=Name(id='self', ctx=Load()), attr='atol', ctx=Load()))])), Return(value=Name(id='self', ctx=Load()))], decorator_list=[], returns=Constant(value='MRMRFeatureSelectionTransform')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='relevance_table', annotation=Name(id='RelevanceTable', ctx=Load())), arg(arg='top_k', annotation=Name(id='int', ctx=Load())), arg(arg='features_to_use', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()), Subscript(value=Name(id='Literal', ctx=Load()), slice=Constant(value='all'), ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='relevance_aggregation_mode', annotation=Name(id='str', ctx=Load())), arg(arg='redundancy_aggregation_mode', annotation=Name(id='str', ctx=Load())), arg(arg='atol', annotation=Name(id='float', ctx=Load())), arg(arg='return_features', annotation=Name(id='bool', ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='relevance_params'), defaults=[Constant(value='all'), Attribute(value=Name(id='AggregationMode', ctx=Load()), attr='mean', ctx=Load()), Attribute(value=Name(id='AggregationMode', ctx=Load()), attr='mean', ctx=Load()), Constant(value=1e-10), Constant(value=False)]), body=[Expr(value=Constant(value='ťI9nit M͟RMRFʹeatˤureSel¶e˱ctionITransform.\n\nParam͖e˭tersȩ\nδ---ɟŪ---ˎ--ʻ--\nrelevanͪce_tableˑ:\nǰ Α   methoƿd toŻ cǳhalcȪȨuƉlate relevance ta͇ble\ntop_k:\n    numϏ ½of feŤatu˥res toèʂ selŏect; if thƴe˗rŤe are ˭Enot eǖnough featɝȪureķs,X the\x96n all will beɥ seƤlectedć\nfeatƕʕurɮes_t͉èo_ήuse:\n    cȀo¯ʕlumns of ĉthe dΨaʌtasetɢ to seΌleŔct frøoȏm\n    if "all\x97"Í value iŧs given̦, all columϿns ȯare usϬƽed\nrelevance_aggregatioɑn_modˋeά:\n  ̉  theɢâ ˋ;methoʃd fori relevance valuȍe˩s per-segme΅n3Ȭt aggregatϽi͡on\nreduð¤Ϯndan.cyé_aggregationª_mode:\n Ƞ   the emet^hod foƄr red/unǍdancΑy vaϱl̼uÅes per-segment ͅaggrĩëgaģtiɳon\natŗol:Ɏ\n    the absolutϭe tǏoleranc˯ôe ́to coŎmp˟arϗe̐ tϱhe ΆflΜoĐat valueɆs\nretʎurn_features:\n    indicǖaˌtes whe*the˭r to rŶeturɼnŲɷ features ]͖ɴor nöt.')), If(test=BoolOp(op=Or(), values=[UnaryOp(op=Not(), operand=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='top_k', ctx=Load()), Name(id='int', ctx=Load())], keywords=[])), Compare(left=Name(id='top_k', ctx=Load()), ops=[Lt()], comparators=[Constant(value=0)])]), body=[Raise(exc=Call(func=Name(id='valueerror', ctx=Load()), args=[Constant(value='Parameter top_k should be positive integer')], keywords=[]))], orelse=[]), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='features_to_use', value=Name(id='features_to_use', ctx=Load())), keyword(arg='return_features', value=Name(id='return_features', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='relevance_table', ctx=Store())], value=Name(id='relevance_table', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='top_k', ctx=Store())], value=Name(id='top_k', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='relevance_aggregation_mode', ctx=Store())], value=Name(id='relevance_aggregation_mode', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='redundancy_aggregation_mode', ctx=Store())], value=Name(id='redundancy_aggregation_mode', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='atol', ctx=Store())], value=Name(id='atol', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='relevance_params', ctx=Store())], value=Name(id='relevance_params', ctx=Load()))], decorator_list=[])], decorator_list=[])], type_ignores=[])