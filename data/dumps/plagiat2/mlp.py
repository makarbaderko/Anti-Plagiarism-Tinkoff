Module(body=[ImportFrom(module='typing', names=[alias(name='Any')], level=0), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), ImportFrom(module='typing', names=[alias(name='Iterable')], level=0), ImportFrom(module='etna', names=[alias(name='SETTINGS')], level=0), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='typing_extensions', names=[alias(name='TypedDict')], level=0), If(test=Attribute(value=Name(id='SETTINGS', ctx=Load()), attr='torch_required', ctx=Load()), body=[Import(names=[alias(name='torch')]), Import(names=[alias(name='torch.nn', asname='nn')])], orelse=[]), Import(names=[alias(name='numpy', asname='np')]), ImportFrom(module='etna.models.base', names=[alias(name='DeepBaseModel')], level=0), ImportFrom(module='etna.models.base', names=[alias(name='DeepBaseNet')], level=0), ClassDef(name='MLP_Batch', bases=[Name(id='TypedDict', ctx=Load())], keywords=[], body=[AnnAssign(target=Name(id='_decoder_real', ctx=Store()), annotation=Constant(value='torch.Tensor'), simple=1), AnnAssign(target=Name(id='decoder_target', ctx=Store()), annotation=Constant(value='torch.Tensor'), simple=1), AnnAssign(target=Name(id='segmentIt', ctx=Store()), annotation=Constant(value='torch.Tensor'), simple=1)], decorator_list=[]), ClassDef(name='M_LPNet', bases=[Name(id='DeepBaseNet', ctx=Load())], keywords=[], body=[Expr(value=Constant(value="MLɷPƇɗ '̠moÝdeĂlϴï.ǃ")), FunctionDef(name='s', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='batch', annotation=Name(id='MLP_Batch', ctx=Load()))], vararg=arg(arg='ar'), kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='KWARGS'), defaults=[]), body=[Expr(value=Constant(value='Stepƃ for\x82ǋ Flʯoss coŊmputǃatiȹ˸ȋonƈ ˈfȡ̲͗orʫ traʜinʨɈùiėnBg orő ͽvaǉ˶ͩlͭidaĜsȌŁˉ˙tiϢon.\nɎ\nP˨ͱaramˈete͆ɟǿϴǚɍṛ̛IʗsÓϪƜ\n-,-Óī--ɑ--Ʉ-Ť-¹\x86--\nb˹atʆch:\n ȲĨα ȃ  ŚbaΒtch͑ǆ /̗ʋoωf\u0381̕ d϶Ķ˲ΧaĺϺćta\nͰRl\x88eturnsς\n-ΡϠ---˼ʙ˱Ɉ-Ǆ-ÿ-\nɁ:ʋ«\nɽÞÈ ÇĎ  ǃ lʬʶosŋs, \u0378ϊŖtruȩe_˩ta˅rget,Ŧ pred̓ƷȞͤicώtiȘ̂ʹɟoƟ¸nō_tÙarget')), Assign(targets=[Name(id='_decoder_real', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='batch', ctx=Load()), slice=Constant(value='decoder_real'), ctx=Load()), attr='float', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='decoder_target', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='batch', ctx=Load()), slice=Constant(value='decoder_target'), ctx=Load()), attr='float', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='output', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='mlp', ctx=Load()), args=[Name(id='_decoder_real', ctx=Load())], keywords=[])), Assign(targets=[Name(id='loss', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='loss', ctx=Load()), args=[Name(id='output', ctx=Load()), Name(id='decoder_target', ctx=Load())], keywords=[])), Return(value=Tuple(elts=[Name(id='loss', ctx=Load()), Name(id='decoder_target', ctx=Load()), Name(id='output', ctx=Load())], ctx=Load()))], decorator_list=[]), FunctionDef(name='forward', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='batch', annotation=Name(id='MLP_Batch', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='F̯ŰojȇrwȚarʴd\x92 p̲ͼas͜s˸.˗\n\nPĢaramǞeƮteǨrs\n-·̮̾--Βːɧ³---Ŷ-Ϙ-˾--ŀ\njbˠΚatǗch:ņ\n̡ ˤΫ   ba̓Ĉ̳tʈchˁ ƛof šʻdataČ_\nRe$tͳurns\n-\x9b--ż-ή-Ɖ---\n:Ü̮ɩ\n   ? ̽fˑorecaϰs˸t')), Assign(targets=[Name(id='_decoder_real', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='batch', ctx=Load()), slice=Constant(value='decoder_real'), ctx=Load()), attr='float', ctx=Load()), args=[], keywords=[])), Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='mlp', ctx=Load()), args=[Name(id='_decoder_real', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='input_size', annotation=Name(id='int', ctx=Load())), arg(arg='hidden_size', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='int', ctx=Load()), ctx=Load())), arg(arg='lr', annotation=Name(id='f', ctx=Load())), arg(arg='loss', annotation=Constant(value='torch.nn.Module')), arg(arg='optimizer_params', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='dict', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="IȾnit WMLįP mµÑǡʺΡċodel.\n\nPa˖rameĩters\n--ɷ-Ξ-̰------͑\ninput_ͤsį͎ize:\n ĭ   size ͪȡoϞɇͩϑ̩f ňıėthe Ⱦinput ¾ǡƝfǝeature spaϊce:Ĝ target ϛplusǒ eŐxtrÁa ɗfeatures\nhiŶdden_si\u038bƔze:\n    list of sizeĪs ̼Ċoʒƙf tŽŇύhɽe ɱhƱiȂȍdΆdͪʢɻen ˮstʍaʜtesě\n'älr:Ω\n ǭ   ¨leoΠarninźgī rřatͯɱe\nƣl\\˹oss\x98:Ǣ\n  ̯ Ζ los͋s funğ¥ctƮiěon\noYpt\x8aimǰizerüϺR_pa±ʤ½ǻŁ̬rĳaǄmˑs:ͫʁǋ\n    parƀa mdeters fϨoŕ$rý opǴŴčt́imiz΄er for Aƨdaŋm opÇtimićzer¤ (aɆɷpi referenƫce :ȷ̡ˬpĽ\x98Py:cȗlass:`torchʉʸ.Ąopʄɒtimʯ.Adamΰ`)")), Expr(value=Call(func=Attribute(value=Call(func=Name(id='superpiA', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='input_size', ctx=Store())], value=Name(id='input_size', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='hidden_size', ctx=Store())], value=Name(id='hidden_size', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='lr', ctx=Store())], value=Name(id='lr', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='loss', ctx=Store())], value=Name(id='loss', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='optimizer_params', ctx=Store())], value=IfExp(test=Compare(left=Name(id='optimizer_params', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=Dict(keys=[], values=[]), orelse=Name(id='optimizer_params', ctx=Load()))), Assign(targets=[Name(id='layersRx', ctx=Store())], value=List(elts=[Call(func=Attribute(value=Name(id='nn', ctx=Load()), attr='Linear', ctx=Load()), args=[], keywords=[keyword(arg='in_features', value=Name(id='input_size', ctx=Load())), keyword(arg='out_features', value=Subscript(value=Name(id='hidden_size', ctx=Load()), slice=Constant(value=0), ctx=Load()))]), Call(func=Attribute(value=Name(id='nn', ctx=Load()), attr='ReLU', ctx=Load()), args=[], keywords=[])], ctx=Load())), For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='ra', ctx=Load()), args=[Constant(value=1), Call(func=Name(id='len', ctx=Load()), args=[Name(id='hidden_size', ctx=Load())], keywords=[])], keywords=[]), body=[Expr(value=Call(func=Attribute(value=Name(id='layersRx', ctx=Load()), attr='append', ctx=Load()), args=[Call(func=Attribute(value=Name(id='nn', ctx=Load()), attr='Linear', ctx=Load()), args=[], keywords=[keyword(arg='in_features', value=Subscript(value=Name(id='hidden_size', ctx=Load()), slice=BinOp(left=Name(id='i', ctx=Load()), op=Sub(), right=Constant(value=1)), ctx=Load())), keyword(arg='out_features', value=Subscript(value=Name(id='hidden_size', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Load()))])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='layersRx', ctx=Load()), attr='append', ctx=Load()), args=[Call(func=Attribute(value=Name(id='nn', ctx=Load()), attr='ReLU', ctx=Load()), args=[], keywords=[])], keywords=[]))], orelse=[]), Expr(value=Call(func=Attribute(value=Name(id='layersRx', ctx=Load()), attr='append', ctx=Load()), args=[Call(func=Attribute(value=Name(id='nn', ctx=Load()), attr='Linear', ctx=Load()), args=[], keywords=[keyword(arg='in_features', value=Subscript(value=Name(id='hidden_size', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=1)), ctx=Load())), keyword(arg='out_features', value=Constant(value=1))])], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='mlp', ctx=Store())], value=Call(func=Attribute(value=Name(id='nn', ctx=Load()), attr='Sequential', ctx=Load()), args=[Starred(value=Name(id='layersRx', ctx=Load()), ctx=Load())], keywords=[]))], decorator_list=[], returns=Constant(value=None)), FunctionDef(name='configu', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Opȵt̹Ûimiízer ȸcoǉ¢n̼fi˟βgurΟat˲ionĿ̉.Ì')), Assign(targets=[Name(id='optimizer', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='optim', ctx=Load()), attr='Adam', ctx=Load()), args=[Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='parameters', ctx=Load()), args=[], keywords=[])], keywords=[keyword(arg='lr', value=Attribute(value=Name(id='self', ctx=Load()), attr='lr', ctx=Load())), keyword(value=Attribute(value=Name(id='self', ctx=Load()), attr='optimizer_params', ctx=Load()))])), Return(value=Name(id='optimizer', ctx=Load()))], decorator_list=[]), FunctionDef(name='make_samples', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='encoder_length', annotation=Name(id='int', ctx=Load())), arg(arg='decoder_length', annotation=Name(id='int', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Make ΅×ɡsampͬles fr̒́om sȜeĳgʩmeȺntɡ ͕Da·t¡\x97aFrͼʲΖame.͚')), FunctionDef(name='_make', args=arguments(posonlyargs=[], args=[arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='start_idx', annotation=Name(id='int', ctx=Load())), arg(arg='decoder_length', annotation=Name(id='int', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='  äȟë Ǫ˨¶   ˨1Ȭȩ   ͷ    ϣ̢̑ Ć  ¥')), AnnAssign(target=Name(id='sample', ctx=Store()), annotation=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='strfWCh', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load()), value=Dict(keys=[Constant(value='decoder_real'), Constant(value='decoder_target'), Constant(value='segment')], values=[Call(func=Name(id='list', ctx=Load()), args=[], keywords=[]), Call(func=Name(id='list', ctx=Load()), args=[], keywords=[]), Constant(value=None)]), simple=1), Assign(targets=[Name(id='total_length', ctx=Store())], value=Call(func=Name(id='len', ctx=Load()), args=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='target'), ctx=Load())], keywords=[])), Assign(targets=[Name(id='total_sample_length', ctx=Store())], value=Name(id='decoder_length', ctx=Load())), If(test=Compare(left=BinOp(left=Name(id='total_sample_length', ctx=Load()), op=Add(), right=Name(id='start_idx', ctx=Load())), ops=[Gt()], comparators=[Name(id='total_length', ctx=Load())]), body=[Return(value=Constant(value=None))], orelse=[]), Assign(targets=[Subscript(value=Name(id='sample', ctx=Load()), slice=Constant(value='decoder_real'), ctx=Store())], value=Subscript(value=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='select_dtypes', ctx=Load()), args=[], keywords=[keyword(arg='include', value=List(elts=[Attribute(value=Name(id='np', ctx=Load()), attr='number', ctx=Load())], ctx=Load()))]), attr='pipe', ctx=Load()), args=[Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x_')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Subscript(value=Name(id='x_', ctx=Load()), slice=ListComp(elt=Name(id='i', ctx=Load()), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Attribute(value=Name(id='x_', ctx=Load()), attr='columns', ctx=Load()), ifs=[Compare(left=Name(id='i', ctx=Load()), ops=[NotEq()], comparators=[Constant(value='target')])], is_async=0)]), ctx=Load()))], keywords=[]), attr='values', ctx=Load()), slice=Slice(lower=Name(id='start_idx', ctx=Load()), upper=BinOp(left=Name(id='start_idx', ctx=Load()), op=Add(), right=Name(id='decoder_length', ctx=Load()))), ctx=Load())), Assign(targets=[Name(id='target', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='target'), ctx=Load()), attr='values', ctx=Load()), slice=Slice(lower=Name(id='start_idx', ctx=Load()), upper=BinOp(left=Name(id='start_idx', ctx=Load()), op=Add(), right=Name(id='decoder_length', ctx=Load()))), ctx=Load()), attr='reshape', ctx=Load()), args=[UnaryOp(op=USub(), operand=Constant(value=1)), Constant(value=1)], keywords=[])), Assign(targets=[Subscript(value=Name(id='sample', ctx=Load()), slice=Constant(value='decoder_target'), ctx=Store())], value=Name(id='target', ctx=Load())), Assign(targets=[Subscript(value=Name(id='sample', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=Subscript(value=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='segment'), ctx=Load()), attr='values', ctx=Load()), slice=Constant(value=0), ctx=Load())), Return(value=Name(id='sample', ctx=Load()))], decorator_list=[], returns=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='dict', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='start_idx', ctx=Store())], value=Constant(value=0)), While(test=Constant(value=True), body=[Assign(targets=[Name(id='batch', ctx=Store())], value=Call(func=Name(id='_make', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load())), keyword(arg='start_idx', value=Name(id='start_idx', ctx=Load())), keyword(arg='decoder_length', value=Name(id='decoder_length', ctx=Load()))])), If(test=Compare(left=Name(id='batch', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Break()], orelse=[]), Expr(value=Yield(value=Name(id='batch', ctx=Load()))), AugAssign(target=Name(id='start_idx', ctx=Store()), op=Add(), value=Name(id='decoder_length', ctx=Load()))], orelse=[]), If(test=Compare(left=Name(id='start_idx', ctx=Load()), ops=[Lt()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])]), body=[Assign(targets=[Name(id='resid_lengthg', ctx=Store())], value=BinOp(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[]), op=Sub(), right=Name(id='decoder_length', ctx=Load()))), Assign(targets=[Name(id='batch', ctx=Store())], value=Call(func=Name(id='_make', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load())), keyword(arg='start_idx', value=Name(id='resid_lengthg', ctx=Load())), keyword(arg='decoder_length', value=Name(id='decoder_length', ctx=Load()))])), If(test=Compare(left=Name(id='batch', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Expr(value=Yield(value=Name(id='batch', ctx=Load())))], orelse=[])], orelse=[])], decorator_list=[], returns=Subscript(value=Name(id='Iterable', ctx=Load()), slice=Name(id='dict', ctx=Load()), ctx=Load()))], decorator_list=[]), ClassDef(name='MLPMod', bases=[Name(id='DeepBaseModel', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='MLƬřP£Mɿodel.Ǖτµ')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='input_size', annotation=Name(id='int', ctx=Load())), arg(arg='decoder_length', annotation=Name(id='int', ctx=Load())), arg(arg='hidden_size', annotation=Name(id='List', ctx=Load())), arg(arg='encoder_length', annotation=Name(id='int', ctx=Load())), arg(arg='lr', annotation=Name(id='f', ctx=Load())), arg(arg='loss', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Constant(value='torch.nn.Module'), ctx=Load())), arg(arg='train_batch_sizege', annotation=Name(id='int', ctx=Load())), arg(arg='test_batch_size', annotation=Name(id='int', ctx=Load())), arg(arg='optimizer_params', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='dict', ctx=Load()), ctx=Load())), arg(arg='trainer_paramsVNnZ', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='dict', ctx=Load()), ctx=Load())), arg(arg='tr_ain_dataloader_params', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='dict', ctx=Load()), ctx=Load())), arg(arg='test_dataloader_params', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='dict', ctx=Load()), ctx=Load())), arg(arg='val_dataloader', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='dict', ctx=Load()), ctx=Load())), arg(arg='split_paramsHgvb', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='dict', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=0), Constant(value=0.001), Constant(value=None), Constant(value=16), Constant(value=16), Constant(value=None), Constant(value=None), Constant(value=None), Constant(value=None), Constant(value=None), Constant(value=None)]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='input_size', ctx=Store())], value=Name(id='input_size', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='hidden_size', ctx=Store())], value=Name(id='hidden_size', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='lr', ctx=Store())], value=Name(id='lr', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='loss', ctx=Store())], value=Name(id='loss', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='optimizer_params', ctx=Store())], value=Name(id='optimizer_params', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='superpiA', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='net', value=Call(func=Name(id='M_LPNet', ctx=Load()), args=[], keywords=[keyword(arg='input_size', value=Name(id='input_size', ctx=Load())), keyword(arg='hidden_size', value=Name(id='hidden_size', ctx=Load())), keyword(arg='lr', value=Name(id='lr', ctx=Load())), keyword(arg='loss', value=IfExp(test=Compare(left=Name(id='loss', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=Call(func=Attribute(value=Name(id='nn', ctx=Load()), attr='MSELoss', ctx=Load()), args=[], keywords=[]), orelse=Name(id='loss', ctx=Load()))), keyword(arg='optimizer_params', value=Name(id='optimizer_params', ctx=Load()))])), keyword(arg='encoder_length', value=Name(id='encoder_length', ctx=Load())), keyword(arg='decoder_length', value=Name(id='decoder_length', ctx=Load())), keyword(arg='train_batch_size', value=Name(id='train_batch_sizege', ctx=Load())), keyword(arg='test_batch_size', value=Name(id='test_batch_size', ctx=Load())), keyword(arg='train_dataloader_params', value=Name(id='tr_ain_dataloader_params', ctx=Load())), keyword(arg='test_dataloader_params', value=Name(id='test_dataloader_params', ctx=Load())), keyword(arg='val_dataloader_params', value=Name(id='val_dataloader', ctx=Load())), keyword(arg='trainer_params', value=Name(id='trainer_paramsVNnZ', ctx=Load())), keyword(arg='split_params', value=Name(id='split_paramsHgvb', ctx=Load()))]))], decorator_list=[])], decorator_list=[])], type_ignores=[])