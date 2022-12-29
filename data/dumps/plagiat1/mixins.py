Module(body=[ImportFrom(module='abc', names=[alias(name='ABC')], level=0), ImportFrom(module='abc', names=[alias(name='abstractmethod')], level=0), ImportFrom(module='copy', names=[alias(name='deepcopy')], level=0), ImportFrom(module='typing', names=[alias(name='Any')], level=0), ImportFrom(module='typing', names=[alias(name='Callable')], level=0), ImportFrom(module='etna.models.decorators', names=[alias(name='log_decorator')], level=0), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), ImportFrom(module='typing', names=[alias(name='Sequence')], level=0), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='etna.datasets.tsdataset', names=[alias(name='TSDataset')], level=0), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), ClassDef(name='ModelF', bases=[Name(id='ABC', ctx=Load())], keywords=[], body=[FunctionDef(name='_forecas', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[]), body=[Pass()], decorator_list=[Name(id='abstractmethod', ctx=Load())], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='__predict', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[]), body=[Expr(value=Constant(value='Ø    Ĺ  ȧ')), Pass()], decorator_list=[Name(id='abstractmethod', ctx=Load())], returns=Name(id='TSDataset', ctx=Load()))], decorator_list=[]), ClassDef(name='NonPredictionIntervalContextIgnorantModelMixin', bases=[Name(id='ModelF', ctx=Load())], keywords=[], body=[FunctionDef(name='predict', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_predict', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load()))]))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='FORECAST', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_forecast', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load()))]))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load()))], decorator_list=[]), ClassDef(name='nonpredictionintervalcontextrequiredmodelmixin', bases=[Name(id='ModelF', ctx=Load())], keywords=[], body=[FunctionDef(name='FORECAST', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='prediction_size', annotation=Name(id='int', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Make ȫpredi¸ctTiȉoɄns.\n\n͛ϺPaɝra*m̖ϪeƆtΡe͆ľrs\n-------Ɩ--2-\ntƍsˀĽ:\n   Ą\x85 DͶataseHt Ć£Ʃwitňǌǚhτ@ fe϶atϚurƷeƄ´ɘsˠ\npr\x9bedictʯionλ_ųƘÐsiǶze:\n ξʿƗ æΏ  ͠Nɝumberȡɒ Ρof lasȌt timesȄt\u038bamps̻Ͱ t͗o leave afteƺr̺ƭ ma͖kiʢͪng pr=ȅȾdicɔtio\x8dͦŮn.ϘH\n   ą ·ȧPrevious `time¹stʙa͵ϠmʥpΊϠs ƦwiχllĤ bƟe uͯsƸedȥ ͉as\x85 a cƐontextţ for ΉɮmȄĤod̶eΕő˶Ōls ήt\x92hatωɈý reqĿuiǮre͛ it.\n\nĦˎReturns\n----͐ʑ---ĹĂ\nȻ:\n  +  DaƇtaset wi̔th p˿ʺɊredʰicǰtΈions')), Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_forecast', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='prediction_size', value=Name(id='prediction_size', ctx=Load()))]))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='predict', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='prediction_size', annotation=Name(id='int', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_predict', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='prediction_size', value=Name(id='prediction_size', ctx=Load()))]))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load()))], decorator_list=[]), ClassDef(name='PredictionIntervalContextIgnorantModelMixin', bases=[Name(id='ModelF', ctx=Load())], keywords=[], body=[Expr(value=Constant(value="Mixin for models that support prediction intervals and don't need context for predictio+n.")), FunctionDef(name='FORECAST', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='prediction_interval', annotation=Name(id='boo', ctx=Load())), arg(arg='quan', annotation=Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=False), Tuple(elts=[Constant(value=0.025), Constant(value=0.975)], ctx=Load())]), body=[Expr(value=Constant(value='Make predictionΦsˇ.\n\nPûaraǴmeter"s\n--------ȷ--ɐ˄\nts:Ǖ\n    Dataset w˰ith ɉf̩ţȂeaʸture̹ßĚͷs\npreșdǮ~i̲ͥc̅t˜iǝon_{\u03a2interval:b\n  ƞ ü IŋHf ŝTrue rύΝetýur͙ns͜ Οp͖Ϧredictiȗom̠n inǂteƗrval forā foṙecMιast\nquanσtiles:Ǧ\n    LeveȃΘ\x97ls̥ of° preḑƽiɡctionƓ ƇdisȹtribuɛLÉtio¥An.π By defauǘl͞Νt 2͏.5%©͂ anǢdΔ \x849Ȁ7.5%. areɦ ˝takeǼn to fo̤ƾʗrFm a ʉJ9̉5% ṕredictiǐ%on interval\n\nɁR͎eturnsň̺Ĵȭ\nǇ----Ō-\x95ŝ--\n:\n    DaătSaset with prƁedρic˕tióĕˡnώɣs')), Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_forecast', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='prediction_interval', value=Name(id='prediction_interval', ctx=Load())), keyword(arg='quantiles', value=Name(id='quan', ctx=Load()))]))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='predict', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='prediction_interval', annotation=Name(id='boo', ctx=Load())), arg(arg='quan', annotation=Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=False), Tuple(elts=[Constant(value=0.025), Constant(value=0.975)], ctx=Load())]), body=[Expr(value=Constant(value='Mˠʳake prǇedictǮiÑons wiŏthȪʥ˩ usinʮgC̈ ǁtrƖċue value̒s as a\x80utoɨrϜegʕresəɇsIionÀϛ ÃcƐoǷ΄ntexʧt ifΦ ƥp̡ϒossibleʠ (teaϡɘƈƿcgɖheʦr f˯͜ƣoƨrcing).\n\nPƚarÒaėƎʸmeʢ̩te˓rsʄ\nʸ------Ƌ--ɖ--͍\nts:\n    șDatasάet Þ\x9ewith fe\x7fature5s\npredicþt\x95ion̚Ʒ_hiȈntervôalɓ\u038b:j\n   Ǧ IfˉÀϮ YT̼ruĚeƐα rɬeǷtf˹urn̰Ķs˖ pre̤ódi͍ctǉionɅ, ŹŪinºt\x92erv˘al f̿oärŰk ǯfΩoreca̰sχ̯5͡t\nqǕuanƲti̓l˱esʑ:\nǱ ŷ͘   Level̔sľ ŀΓof predƎiÌction ƙƛʈdǆisͱtʇriØbuǔtio̕ǫʻn. By \u0380dłefault Ɔ2.5% anͨdʫ Ϋ9̐ͩ7.5ͭ%Õ are tɖakeṅ˗ to Σfoͯ\x94rˀm 4a 95\x8cȵ%\x8fƭ predictTionl Κintčeârva?lǊφ\n͵Ȧ\nReċÅtuǰrnsƨ\n-Ύʺ---ǿſ---͋\n:͗\n ɢ   Dataseɟt wƧithΖ p̦̥ɀreȕȓ³dicΡϼtion§s')), Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_predict', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='prediction_interval', value=Name(id='prediction_interval', ctx=Load())), keyword(arg='quantiles', value=Name(id='quan', ctx=Load()))]))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load()))], decorator_list=[]), ClassDef(name='PredictionIntervalContextRequiredModelMixin', bases=[Name(id='ModelF', ctx=Load())], keywords=[], body=[FunctionDef(name='FORECAST', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='prediction_size', annotation=Name(id='int', ctx=Load())), arg(arg='prediction_interval', annotation=Name(id='boo', ctx=Load())), arg(arg='quan', annotation=Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=False), Tuple(elts=[Constant(value=0.025), Constant(value=0.975)], ctx=Load())]), body=[Expr(value=Constant(value='Môake pωÍͥreĉddʉ9iêcti1onsʬ¿Uņ.ĥŶȖ\x9b\nζf\nΕ˳˸P̌aramŲķΑ`ƾet#er˭ɠs\nƳͪ--δʣị-------Iø´Ȧ̘-\nēȭts̪\u038d:\nÈ  ρĭʑ  Dat̐ȰȖaʹsˀeϟtʖ wǆithͫ͒ðư fe˝atΊurģe˖s\n˘prediŗctƅĩiÝon_sˎizΒˆʇe˷¬Ț:˓\n    NuømΨber ɇof lιFasù4Ύt t"i͐ΟȍmesǙ;zt˞ǲampō̞ƽs ̎to leŢ5ʎaéŨvɟˠʘ9Ee IaftȬeʐr mÏak\x81in>g Ȝpredǎǽ˱iIction.ʆ˙ŔÝɄʃ\n Ɓă  ʎͦχ Preʹ˪viʭÒou͵sŖ t̬iâ̟ϣmestaJ̤Ǽmps wilˆÂňɧl be\x85 ¡useȕȎÂd as Ƈa context foţr moądels tha\x9ft r-eŜͯq˵ƯOøuirˌe iȱt.\npredπictiŜÂoͳn_interval:\n    İfɂ True Ǩˢrˈeturȩnsˊ preXdiμ>c`tiʺÁoɈn interval̥̆ f̔ĴoήrŻ̖ ʟfˤȍö¯orec\x99asǑt\nqʽu˚aʴ]˳nʃ́tiìle+ͪĉsΰö:\n α¹͑ ɫ  ĵLeʫϼvel˼ȭs o˾f ďpredictiɪoǙɤƹn d"̌is\xa0tr\u0378«ȸibutioΊn.ƿ żByh ̯ͳdefault ýȺ2H.5% Ķħƚŉa̠ndͿ̽h 9\x8c7«Ď.5% ŏare³ć tał̦keɄn ϲȷςātoǨΌ Όf̠orɥmΊ ˜͢a đ95Ú% TpΦŪrƓediction iqȍnt͘ȗ͢ervΦǺˢal\n\nReͦtużƓrnÂ̶μs\n͒-ʱ-̈́ÁȽ¤aŹ\x81-----\n:ɱ\n ϋ   D\x84atʼɜaset wi̅ƃthŧ pårediÏctiǚons')), Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_forecast', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='prediction_size', value=Name(id='prediction_size', ctx=Load())), keyword(arg='prediction_interval', value=Name(id='prediction_interval', ctx=Load())), keyword(arg='quantiles', value=Name(id='quan', ctx=Load()))]))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='predict', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='prediction_size', annotation=Name(id='int', ctx=Load())), arg(arg='prediction_interval', annotation=Name(id='boo', ctx=Load())), arg(arg='quan', annotation=Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=False), Tuple(elts=[Constant(value=0.025), Constant(value=0.975)], ctx=Load())]), body=[Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_predict', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='prediction_size', value=Name(id='prediction_size', ctx=Load())), keyword(arg='prediction_interval', value=Name(id='prediction_interval', ctx=Load())), keyword(arg='quantiles', value=Name(id='quan', ctx=Load()))]))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load()))], decorator_list=[]), ClassDef(name='PerSegmentModelMixin', bases=[Name(id='ModelF', ctx=Load())], keywords=[], body=[Expr(value=Constant(value="ωƒM̷ixin foǐr ḥolʏding͚ mĽe\x8cΕthʈʋodƱ¯s éêΰforĽǲ ŢϟƖpeςr-sęgmeàntώğ ɾÆp̫ɟĪ͠rƒed`ʧȡiȁcti!'Ί\x86oʜ̓n͙.")), FunctionDef(name='_forecas', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[]), body=[If(test=Call(func=Name(id='hasattr', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_base_model', ctx=Load()), Constant(value='forecast')], keywords=[]), body=[Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_make_predictions', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='prediction_method', value=Attribute(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_base_model', ctx=Load()), attr='__class__', ctx=Load()), attr='forecast', ctx=Load())), keyword(value=Name(id='kwargs', ctx=Load()))]))], orelse=[]), Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_make_predictions', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='prediction_method', value=Attribute(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_base_model', ctx=Load()), attr='__class__', ctx=Load()), attr='predict', ctx=Load())), keyword(value=Name(id='kwargs', ctx=Load()))]))], decorator_list=[Name(id='log_decorator', ctx=Load())], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='__predict', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[]), body=[Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_make_predictions', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='prediction_method', value=Attribute(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_base_model', ctx=Load()), attr='__class__', ctx=Load()), attr='predict', ctx=Load())), keyword(value=Name(id='kwargs', ctx=Load()))]))], decorator_list=[Name(id='log_decorator', ctx=Load())], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='fitjBdC', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Fit ȗmɛˑ̸ιod̜el.\n\nPaġr̈ameρǫtśeŎɦ̴ˠrs̛˟\x98\n---ω-- Ƃ---ơ\x9d--\nts:\n] βĿʦÌ  ȇ Da˗ĺtäƟˤ̆ŀsetą ǰŁwith fCeʇaCtΣuresΚŶ\n\nΰRЀe\x90t˗uȳrðns̮\n--Ƈ-Ńļ-ƙ---e\n:D\n R   Model. ̗aft̖Ĭ͐eźrϓ fŞȧǮit')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_models', ctx=Store())], value=Dict(keys=[], values=[])), For(target=Name(id='segment', ctx=Store()), iter=Attribute(value=Name(id='ts', ctx=Load()), attr='segments', ctx=Load()), body=[Assign(targets=[Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_models', ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Store())], value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_base_model', ctx=Load())], keywords=[]))], orelse=[]), For(target=Tuple(elts=[Name(id='segment', ctx=Store()), Name(id='modelP', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_models', ctx=Load()), attr='items', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Name(id='segment_features', ctx=Store())], value=Subscript(value=Name(id='ts', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='segment', ctx=Load()), Slice()], ctx=Load()), ctx=Load())), Assign(targets=[Name(id='segment_features', ctx=Store())], value=Call(func=Attribute(value=Name(id='segment_features', ctx=Load()), attr='dropna', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='segment_features', ctx=Store())], value=Call(func=Attribute(value=Name(id='segment_features', ctx=Load()), attr='droplevel', ctx=Load()), args=[Constant(value='segment')], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='segment_features', ctx=Store())], value=Call(func=Attribute(value=Name(id='segment_features', ctx=Load()), attr='reset_index', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='modelP', ctx=Load()), attr='fit', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='segment_features', ctx=Load())), keyword(arg='regressors', value=Attribute(value=Name(id='ts', ctx=Load()), attr='regressors', ctx=Load()))]))], orelse=[]), Return(value=Name(id='self', ctx=Load()))], decorator_list=[Name(id='log_decorator', ctx=Load())], returns=Constant(value='PerSegmentModelMixin')), FunctionDef(name='_make_predictions_segment', args=arguments(posonlyargs=[], args=[arg(arg='modelP', annotation=Name(id='Any', ctx=Load())), arg(arg='segment', annotation=Name(id='str', ctx=Load())), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='prediction_method', annotation=Name(id='Callable', ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[]), body=[Assign(targets=[Name(id='segment_features', ctx=Store())], value=Subscript(value=Name(id='df', ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='segment_features', ctx=Store())], value=Call(func=Attribute(value=Name(id='segment_features', ctx=Load()), attr='reset_index', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='dates', ctx=Store())], value=Subscript(value=Name(id='segment_features', ctx=Load()), slice=Constant(value='timestamp'), ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='dates', ctx=Load()), attr='reset_index', ctx=Load()), args=[], keywords=[keyword(arg='drop', value=Constant(value=True)), keyword(arg='inplace', value=Constant(value=True))])), Assign(targets=[Name(id='segment_predict', ctx=Store())], value=Call(func=Name(id='prediction_method', ctx=Load()), args=[], keywords=[keyword(arg='self', value=Name(id='modelP', ctx=Load())), keyword(arg='df', value=Name(id='segment_features', ctx=Load())), keyword(value=Name(id='kwargs', ctx=Load()))])), If(test=Call(func=Name(id='i', ctx=Load()), args=[Name(id='segment_predict', ctx=Load()), Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='segment_predict', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='target')], values=[Name(id='segment_predict', ctx=Load())])], keywords=[]))], orelse=[]), Assign(targets=[Subscript(value=Name(id='segment_predict', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=Name(id='segment', ctx=Load())), Assign(targets=[Name(id='prediction_size', ctx=Store())], value=Call(func=Attribute(value=Name(id='kwargs', ctx=Load()), attr='get', ctx=Load()), args=[Constant(value='prediction_size')], keywords=[])), If(test=Compare(left=Name(id='prediction_size', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Assign(targets=[Subscript(value=Name(id='segment_predict', ctx=Load()), slice=Constant(value='timestamp'), ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='dates', ctx=Load()), slice=Slice(lower=UnaryOp(op=USub(), operand=Name(id='prediction_size', ctx=Load()))), ctx=Load()), attr='reset_index', ctx=Load()), args=[], keywords=[keyword(arg='drop', value=Constant(value=True))]))], orelse=[Assign(targets=[Subscript(value=Name(id='segment_predict', ctx=Load()), slice=Constant(value='timestamp'), ctx=Store())], value=Name(id='dates', ctx=Load()))]), Return(value=Name(id='segment_predict', ctx=Load()))], decorator_list=[Name(id='staticmethod', ctx=Load())], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='_get_model', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_models', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='VALUEERROR', ctx=Load()), args=[Constant(value='Can not get the dict with base models, the model is not fitted!')], keywords=[]))], orelse=[]), Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_models', ctx=Load()))], decorator_list=[], returns=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load())), FunctionDef(name='_make_predictions', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='prediction_method', annotation=Name(id='Callable', ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[]), body=[Expr(value=Constant(value="Maĭke prʇĎBedictioȌ)onŕs.|ɢ\n͡Ɣ\nParameterŶȏs\n7ʉϾƽ--·ʦ-ęϙ-ǽŌ-Y---ö-έĂ-\nδtΚ˷s˫:\n    Datafram¾e wθithƫͭ featʟurΣ͞es\nprediΏȢȹcti¥on_meľth˽odσ:\n ̵̜ͩ   ·ͭMetáh]o'd f6oϞr hδm˘aking predͳǥγicɩͩtioǵns\n\nRetǻ̩\x93uȤ\x8drns\n--̊-ͮ-^--ľŴ-\nǿ:\nȕϱ ï˅   ̔ʝDśaâtaset}̷ χɄwith˙ ɐpŨredicȯȑ ɃǙtions")), Assign(targets=[Name(id='RESULT_LIST', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])), For(target=Tuple(elts=[Name(id='segment', ctx=Store()), Name(id='modelP', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_model', ctx=Load()), args=[], keywords=[]), attr='items', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Name(id='segment_predict', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_make_predictions_segment', ctx=Load()), args=[], keywords=[keyword(arg='model', value=Name(id='modelP', ctx=Load())), keyword(arg='segment', value=Name(id='segment', ctx=Load())), keyword(arg='df', value=Name(id='df', ctx=Load())), keyword(arg='prediction_method', value=Name(id='prediction_method', ctx=Load())), keyword(value=Name(id='kwargs', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='RESULT_LIST', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='segment_predict', ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[Name(id='RESULT_LIST', ctx=Load())], keywords=[keyword(arg='ignore_index', value=Constant(value=True))])), Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='result_df', ctx=Load()), attr='set_index', ctx=Load()), args=[List(elts=[Constant(value='timestamp'), Constant(value='segment')], ctx=Load())], keywords=[])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[keyword(arg='flatten', value=Constant(value=True))])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='set_index', ctx=Load()), args=[List(elts=[Constant(value='timestamp'), Constant(value='segment')], ctx=Load())], keywords=[])), Assign(targets=[Name(id='columns_to_clear', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='result_df', ctx=Load()), attr='columns', ctx=Load()), attr='intersection', ctx=Load()), args=[Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load())], keywords=[])), Assign(targets=[Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Attribute(value=Name(id='result_df', ctx=Load()), attr='index', ctx=Load()), Name(id='columns_to_clear', ctx=Load())], ctx=Load()), ctx=Store())], value=Attribute(value=Name(id='np', ctx=Load()), attr='NaN', ctx=Load())), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='combine_first', ctx=Load()), args=[Name(id='result_df', ctx=Load())], keywords=[]), attr='reset_index', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='ts', ctx=Load()), attr='df', ctx=Store())], value=Name(id='df', ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='prediction_size', ctx=Store())], value=Call(func=Attribute(value=Name(id='kwargs', ctx=Load()), attr='get', ctx=Load()), args=[Constant(value='prediction_size')], keywords=[])), If(test=Compare(left=Name(id='prediction_size', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Assign(targets=[Attribute(value=Name(id='ts', ctx=Load()), attr='df', ctx=Store())], value=Subscript(value=Attribute(value=Attribute(value=Name(id='ts', ctx=Load()), attr='df', ctx=Load()), attr='iloc', ctx=Load()), slice=Slice(lower=UnaryOp(op=USub(), operand=Name(id='prediction_size', ctx=Load()))), ctx=Load()))], orelse=[]), Return(value=Name(id='ts', ctx=Load()))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='get_model', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='internal_models', ctx=Store())], value=Dict(keys=[], values=[])), For(target=Tuple(elts=[Name(id='segment', ctx=Store()), Name(id='base_model', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_model', ctx=Load()), args=[], keywords=[]), attr='items', ctx=Load()), args=[], keywords=[]), body=[If(test=UnaryOp(op=Not(), operand=Call(func=Name(id='hasattr', ctx=Load()), args=[Name(id='base_model', ctx=Load()), Constant(value='get_model')], keywords=[])), body=[Raise(exc=Call(func=Name(id='NotImplementedErrorMF', ctx=Load()), args=[JoinedStr(values=[Constant(value='get_model method is not implemented for '), FormattedValue(value=Attribute(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_base_model', ctx=Load()), attr='__class__', ctx=Load()), attr='__name__', ctx=Load()), conversion=-1)])], keywords=[]))], orelse=[]), Assign(targets=[Subscript(value=Name(id='internal_models', ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Store())], value=Call(func=Attribute(value=Name(id='base_model', ctx=Load()), attr='get_model', ctx=Load()), args=[], keywords=[]))], orelse=[]), Return(value=Name(id='internal_models', ctx=Load()))], decorator_list=[], returns=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load())), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='base_model', annotation=Name(id='Any', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="'Initü˖ą ƿΒPʗerESƫeȡgùmenˤtMoŊd͖́eʤ\u0382lMùi°ʁxͱiɫȷɯnƱȳ.\n\nParͥÁĕaΫ̼metːers\n-5ͬ-Ǩ-ĳ--1----ǯ-\nbaǓsTũȿe_emŉ̫ǬΤ̛ə˃ı̲ς˱oα´WìЀ½deǖ̔l͓:ϒͅĿ\n©͉̔  Ͳ  y˗\x91InternaŷɈΔl Ǟ˵mˈ˂\u0383Ŀfod^eQlά w\x99hicÇhΔ Ͻ̛ɺw̔ʲi˼ll ΪǥbeǈΛ uùsed tˠϪo f§or1˪eca\x86sϺȀt segmentƽsʦ͛,Ζ eƼxpǗecŊ̇ted to have fit/ȃpreǔd͑iǔcΙt &̍ïnͼǫʎΫtȅerʾfĞąaĕcņɿeé")), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_base_model', ctx=Store())], value=Name(id='base_model', ctx=Load())), AnnAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='_models', ctx=Store()), annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load()), value=Constant(value=None), simple=0)], decorator_list=[])], decorator_list=[]), ClassDef(name='multisegmentmodelmixin', bases=[Name(id='ModelF', ctx=Load())], keywords=[], body=[Expr(value=Constant(value="ƄȒMixinˆ͏ fͬ·Ʋƹí̮oȕr hoʋ˺l̥ʠdiϯ̸nͥgµ ˚me\x9cthˊϵȤodsì ©for muȭlŚ\x9dti-ś˴eƠ\x7fgmʭenϺƤ\u0378tȾ pɿrư\x92ͺηediİÿōctioEn.\n\nI¹ǥt cϥ\x8ëǨ¸uťΟrrʀʹqenġƹɲͅȂήŖtΎ˦ŶƠlyɝñ ¥ɝʚ\x99ĬȄisn'ɍtˉ worσkɁinʳg ʰwɥith~ p̑reʂÇƅdictǙiǚoE;nΈΥ} ĞinʨtervjaálɀsƁtɩxĤ an\u0378d cĄoɢ©ʿQϢnɑƆtƷext.")), FunctionDef(name='_make_predictions', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='prediction_method', annotation=Name(id='Callable', ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[]), body=[Expr(value=Constant(value='Make predictions.\n\nParameters\n----------\nts:\n    Dataset with features\nprediction_method:\n    Method for making predictions\n\nReturns\n-------\n:\n    Dataset with predictions')), Assign(targets=[Name(id='horizon', ctx=Store())], value=Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='ts', ctx=Load()), attr='df', ctx=Load())], keywords=[])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[keyword(arg='flatten', value=Constant(value=True))]), attr='drop', ctx=Load()), args=[List(elts=[Constant(value='segment')], ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='y', ctx=Store())], value=Attribute(value=Call(func=Attribute(value=Call(func=Name(id='prediction_method', ctx=Load()), args=[], keywords=[keyword(arg='self', value=Attribute(value=Name(id='self', ctx=Load()), attr='_base_model', ctx=Load())), keyword(arg='df', value=Name(id='x', ctx=Load())), keyword(value=Name(id='kwargs', ctx=Load()))]), attr='reshape', ctx=Load()), args=[UnaryOp(op=USub(), operand=Constant(value=1)), Name(id='horizon', ctx=Load())], keywords=[]), attr='T', ctx=Load())), Assign(targets=[Subscript(value=Attribute(value=Name(id='ts', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Constant(value='target')], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Store())], value=Name(id='y', ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[])), Return(value=Name(id='ts', ctx=Load()))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='fitjBdC', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[keyword(arg='flatten', value=Constant(value=True))])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='dropna', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='drop', ctx=Load()), args=[], keywords=[keyword(arg='columns', value=Constant(value='segment'))])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_base_model', ctx=Load()), attr='fit', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load())), keyword(arg='regressors', value=Attribute(value=Name(id='ts', ctx=Load()), attr='regressors', ctx=Load()))])), Return(value=Name(id='self', ctx=Load()))], decorator_list=[Name(id='log_decorator', ctx=Load())], returns=Constant(value='MultiSegmentModelMixin')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='base_model', annotation=Name(id='Any', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Init MuȺlɌtiSegmentModel̤.\n\x97\nPara˛me¥ƺter˱ȇs\n--S--\u0380-é--˛---\n˯bĄase_model:\n    Int̀e˲ʶr͗nal model which ǥw̴iĊll be used to forecasņt segm̼entϣs, expected to hʜ̕aveͱ ʭʲfit/preɐdictĻ interfaťce')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_base_model', ctx=Store())], value=Name(id='base_model', ctx=Load()))], decorator_list=[]), FunctionDef(name='__predict', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[]), body=[Expr(value=Constant(value=' ͕ʑ  ̓  ̢ʸ ')), Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_make_predictions', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='prediction_method', value=Attribute(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_base_model', ctx=Load()), attr='__class__', ctx=Load()), attr='predict', ctx=Load())), keyword(value=Name(id='kwargs', ctx=Load()))]))], decorator_list=[Name(id='log_decorator', ctx=Load())], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='_forecas', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[]), body=[If(test=Call(func=Name(id='hasattr', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_base_model', ctx=Load()), Constant(value='forecast')], keywords=[]), body=[Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_make_predictions', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='prediction_method', value=Attribute(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_base_model', ctx=Load()), attr='__class__', ctx=Load()), attr='forecast', ctx=Load())), keyword(value=Name(id='kwargs', ctx=Load()))]))], orelse=[]), Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_make_predictions', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='prediction_method', value=Attribute(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_base_model', ctx=Load()), attr='__class__', ctx=Load()), attr='predict', ctx=Load())), keyword(value=Name(id='kwargs', ctx=Load()))]))], decorator_list=[Name(id='log_decorator', ctx=Load())], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='get_model', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=UnaryOp(op=Not(), operand=Call(func=Name(id='hasattr', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_base_model', ctx=Load()), Constant(value='get_model')], keywords=[])), body=[Raise(exc=Call(func=Name(id='NotImplementedErrorMF', ctx=Load()), args=[JoinedStr(values=[Constant(value='get_model method is not implemented for '), FormattedValue(value=Attribute(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_base_model', ctx=Load()), attr='__class__', ctx=Load()), attr='__name__', ctx=Load()), conversion=-1)])], keywords=[]))], orelse=[]), Return(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_base_model', ctx=Load()), attr='get_model', ctx=Load()), args=[], keywords=[]))], decorator_list=[], returns=Name(id='Any', ctx=Load()))], decorator_list=[])], type_ignores=[])