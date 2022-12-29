Module(body=[Import(names=[alias(name='numpy', asname='np')]), ImportFrom(names=[alias(name='cgd')], level=1), Import(names=[alias(name='torch')]), Import(names=[alias(name='torchvision')]), ImportFrom(module='third_party', names=[alias(name='efficientnet'), alias(name='ModelM3')], level=3), ImportFrom(module='third_party', names=[alias(name='PyramidNet', asname='PyramidNetImpl')], level=3), ImportFrom(names=[alias(name='bn_inception_simple')], level=1), ImportFrom(module='third_party.cotraining.model', names=[alias(name='resnet', asname='cotraining')], level=3), Import(names=[alias(name='pretrainedmodels')]), ClassDef(name='Cotrai_ningModel', bases=[Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Module', ctx=Load())], keywords=[], body=[FunctionDef(name='cha', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_channels', ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='mean', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='PrĄetό͠ŕrŧ͢a$ġinedÝ mΛod̂\u0381e˼ël˅ 2iũɅnpuϺtȚ nn̉ormalizϿ̃atϱioθ\x9en mea§įn.')), Return(value=List(elts=[Constant(value=0.485), Constant(value=0.456), Constant(value=0.406)], ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='name'), arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=False)]), body=[If(test=Name(id='pretrained', ctx=Load()), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Pretrained co-training models are not available.')], keywords=[]))], orelse=[]), Expr(value=Call(func=Attribute(value=Call(func=Name(id='supe', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Store())], value=Call(func=Call(func=Name(id='getattr', ctx=Load()), args=[Name(id='cotraining', ctx=Load()), Name(id='name', ctx=Load())], keywords=[]), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_channels', ctx=Store())], value=Attribute(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='fc', ctx=Load()), attr='in_features', ctx=Load())), Assign(targets=[Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='avgpool', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Identity', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='fc', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Identity', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), FunctionDef(name='std', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='PretraüoiĦεnedËì ˛modeΓl iŒnput normgaȈ̲l`Ͼiza˯tion ΝzSͦTD.\x7fͪƝ')), Return(value=List(elts=[Constant(value=0.229), Constant(value=0.224), Constant(value=0.225)], ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='inp', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Pretrained model input image size.')), Return(value=Constant(value=224))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='forwardjwhPh', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='input')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='x', ctx=Store())], value=Name(id='input', ctx=Load())), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='layer0', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='layer1', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='layer2', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='layer3', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), If(test=Compare(left=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='layer4', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='layer4', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[]))], orelse=[]), Return(value=Name(id='x', ctx=Load()))], decorator_list=[])], decorator_list=[]), ClassDef(name='TorchVGGModel', bases=[Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Module', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='     ͈ ĸ̅\xa0 Ø  ʚ   ǜǪʃ    ͮėΏ  c')), FunctionDef(name='inp', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ʖPr³ö˃ˢeƿˡtrɎaiϘȋ¿n˻Ħed moVdeϟl inputͱ imØagȞeʸ sizeͣ.')), Return(value=Constant(value=224))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='mean', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=List(elts=[Constant(value=0.485), Constant(value=0.456), Constant(value=0.406)], ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='forwardjwhPh', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='input')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='x', ctx=Store())], value=Name(id='input', ctx=Load())), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='features', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), Return(value=Name(id='x', ctx=Load()))], decorator_list=[]), FunctionDef(name='cha', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ɶNȭʉħu˟ǅ˃mĭbeĽr of ͡oȘutpuçͶt cè̝˸haŒnnels.')), Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_channels', ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='name'), arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=False)]), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='supe', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Store())], value=Call(func=Call(func=Name(id='getattr', ctx=Load()), args=[Attribute(value=Name(id='torchvision', ctx=Load()), attr='models', ctx=Load()), Name(id='name', ctx=Load())], keywords=[]), args=[], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_channels', ctx=Store())], value=Attribute(value=Subscript(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='features', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=3)), ctx=Load()), attr='out_channels', ctx=Load())), Assign(targets=[Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='avgpool', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Identity', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='classifier', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Identity', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), FunctionDef(name='std', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=List(elts=[Constant(value=0.229), Constant(value=0.224), Constant(value=0.225)], ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())])], decorator_list=[]), ClassDef(name='PyramidNet', bases=[Name(id='PyramidNetImpl', ctx=Load())], keywords=[], body=[FunctionDef(name='forwardjwhPh', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='input')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Call(func=Attribute(value=Call(func=Name(id='supe', ctx=Load()), args=[], keywords=[]), attr='features', ctx=Load()), args=[Name(id='input', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='inp', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Prˋetrainead ŊÊ̙mǚodel iɦÔnputχ imagͺeȘƧ sȩize.')), Return(value=Constant(value=224))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='cha', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='NumbeΙr ʉ͈of output channels.')), Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_channels', ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='dataset'), arg(arg='d'), arg(arg='alpha'), arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=False)]), body=[If(test=Name(id='pretrained', ctx=Load()), body=[Raise(exc=Call(func=Name(id='NotImplementedError', ctx=Load()), args=[Constant(value='No pretrained PyramidNet available.')], keywords=[]))], orelse=[]), Expr(value=Call(func=Attribute(value=Call(func=Name(id='supe', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='dataset', ctx=Load())], keywords=[keyword(arg='depth', value=Name(id='d', ctx=Load())), keyword(arg='alpha', value=Name(id='alpha', ctx=Load())), keyword(arg='num_classes', value=Constant(value=1))])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_channels', ctx=Store())], value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='fc', ctx=Load()), attr='in_features', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='avgpool', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Identity', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='fc', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Identity', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), FunctionDef(name='mean', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='PreƹˍtŇrai©n˂\x83\x82ϻʺɯeϴdƲ! Ŝϧmoæ̡ld\x97e͵l̾ inRpśu˭țɋϜ ėnoΉrȠϋmalizoati\\ǼoŠzȢɥʏn ṁea#n.')), Return(value=List(elts=[Constant(value=0.485), Constant(value=0.456), Constant(value=0.406)], ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='std', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Pre·trained moƢdel ʯinput normalization STD.')), Return(value=List(elts=[Constant(value=0.229), Constant(value=0.224), Constant(value=0.225)], ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())])], decorator_list=[]), ClassDef(name='ResNetModel', bases=[Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Module', ctx=Load())], keywords=[], body=[FunctionDef(name='cha', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Number of output channels.')), Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_channels', ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='mean', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=List(elts=[Constant(value=0.485), Constant(value=0.456), Constant(value=0.406)], ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='name'), arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=False)]), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='supe', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Store())], value=Call(func=Call(func=Name(id='getattr', ctx=Load()), args=[Attribute(value=Name(id='torchvision', ctx=Load()), attr='models', ctx=Load()), Name(id='name', ctx=Load())], keywords=[]), args=[], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_channels', ctx=Store())], value=Attribute(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='fc', ctx=Load()), attr='in_features', ctx=Load())), Assign(targets=[Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='avgpool', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Identity', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='fc', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Identity', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), FunctionDef(name='inp', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Pretǋ˚rˈaŝɮ$ineϣdȿ mƐȉodel ɵinp\x85\u0378Čut ϦżÎȽɩiĎmagŏɓe size.K̀')), Return(value=Constant(value=224))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='forwardjwhPh', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='input')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='x', ctx=Store())], value=Name(id='input', ctx=Load())), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='conv1', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='bn1', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='relu', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='maxpool', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='layer1', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='layer2', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='layer3', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='layer4', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), Return(value=Name(id='x', ctx=Load()))], decorator_list=[]), FunctionDef(name='std', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=List(elts=[Constant(value=0.229), Constant(value=0.224), Constant(value=0.225)], ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())])], decorator_list=[]), ClassDef(name='EfficientNet', bases=[Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Module', ctx=Load())], keywords=[], body=[Expr(value=Constant(value=' ͘   Ƌ   ƈΏ     ϙ   Ƅ')), FunctionDef(name='forwardjwhPh', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='input')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='features', ctx=Load()), args=[Name(id='input', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='name'), arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=False)]), body=[Expr(value=Constant(value='oͲ  ')), Expr(value=Call(func=Attribute(value=Call(func=Name(id='supe', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Store())], value=Call(func=Call(func=Name(id='getattr', ctx=Load()), args=[Name(id='efficientnet', ctx=Load()), Name(id='name', ctx=Load())], keywords=[]), args=[], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_channels', ctx=Store())], value=Attribute(value=Subscript(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='classifier', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=1)), ctx=Load()), attr='in_features', ctx=Load())), Assign(targets=[Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='avgpool', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Identity', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='classifier', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Identity', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), FunctionDef(name='mean', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ǄʝPreƤtřraÚineY˿ƺd@˰ modŠe{ʠlʿʬg) ȂiÂʢnpu̱t norĸma͠li̼zatiÚon mŊean.')), Return(value=List(elts=[Constant(value=0.485), Constant(value=0.456), Constant(value=0.406)], ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='cha', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='NĶu̕˂\x7fmͷϮ͂Ύ\x96A\u038bbʕer ofǷϛ oɒu˅tput ch\x97annelaϬs.ʛ')), Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_channels', ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='inp', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Prβʡetrained Ϟmodel input i˴mage siŉze.Ǯ')), Return(value=Constant(value=224))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='std', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=List(elts=[Constant(value=0.229), Constant(value=0.224), Constant(value=0.225)], ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())])], decorator_list=[]), ClassDef(name='PMModel', bases=[Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Module', ctx=Load())], keywords=[], body=[FunctionDef(name='inp', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Try(body=[Return(value=Subscript(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='input_size', ctx=Load()), slice=Constant(value=1), ctx=Load()))], handlers=[ExceptHandler(type=Name(id='attributeerror', ctx=Load()), body=[Raise(exc=Call(func=Name(id='RuntimeError', ctx=Load()), args=[Constant(value='Input size is available only for pretrained models.')], keywords=[]))])], orelse=[], finalbody=[])], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='mean', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='scale', ctx=Store())], value=Subscript(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='input_range', ctx=Load()), slice=Constant(value=1), ctx=Load())), Assign(targets=[Name(id='result', ctx=Store())], value=BinOp(left=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='array', ctx=Load()), args=[Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='mean', ctx=Load())], keywords=[]), op=Div(), right=Name(id='scale', ctx=Load()))), Assign(targets=[Name(id='result', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_adjust_colorspace', ctx=Load()), args=[Subscript(value=Name(id='result', ctx=Load()), slice=Constant(value=None), ctx=Load())], keywords=[]), slice=Constant(value=0), ctx=Load())), Return(value=Name(id='result', ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='std', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='PĘ5rčejȕtÖrƣʽŁǗ˱aine®ˏd mö́del ϕ˛ŁǺiϭnputĉ normaƈġșmlizatiʟǔ˽ˁ%on ͇Ś̕STʮŮDɕŲĞǁ.ĸ')), Assign(targets=[Name(id='scale', ctx=Store())], value=Subscript(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='input_range', ctx=Load()), slice=Constant(value=1), ctx=Load())), Assign(targets=[Name(id='result', ctx=Store())], value=BinOp(left=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='array', ctx=Load()), args=[Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='std', ctx=Load())], keywords=[]), op=Div(), right=Name(id='scale', ctx=Load()))), Assign(targets=[Name(id='result', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_adjust_colorspace', ctx=Load()), args=[Subscript(value=Name(id='result', ctx=Load()), slice=Constant(value=None), ctx=Load())], keywords=[]), slice=Constant(value=0), ctx=Load())), Return(value=Name(id='result', ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='_get_model_', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='name'), arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Call(func=Call(func=Name(id='getattr', ctx=Load()), args=[Name(id='pretrainedmodels', ctx=Load()), Name(id='name', ctx=Load())], keywords=[]), args=[], keywords=[keyword(arg='num_classes', value=Constant(value=1000)), keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))]))], decorator_list=[]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='name'), arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=False)]), body=[Expr(value=Constant(value=' ȏ¬ Ÿɢ˙    Ö  ț      Ǵr   Ϻ   ')), Expr(value=Call(func=Attribute(value=Call(func=Name(id='supe', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='pretrained', ctx=Store())], value=IfExp(test=Name(id='pretrained', ctx=Load()), body=Constant(value='imagenet'), orelse=Constant(value=None))), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_model', ctx=Load()), args=[Name(id='name', ctx=Load())], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_channels', ctx=Store())], value=Attribute(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='last_linear', ctx=Load()), attr='in_features', ctx=Load())), Assign(targets=[Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='global_pool', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Identity', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='last_linear', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Identity', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), FunctionDef(name='cha', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_channels', ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='_adju', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='input')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Subscript(value=Attribute(value=Name(id='input', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=1), ctx=Load()), ops=[NotEq()], comparators=[Constant(value=3)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Bad input shape')], keywords=[]))], orelse=[]), If(test=Compare(left=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='input_space', ctx=Load()), ops=[Eq()], comparators=[Constant(value='RGB')]), body=[Return(value=Name(id='input', ctx=Load()))], orelse=[]), Assert(test=Compare(left=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='input_space', ctx=Load()), ops=[Eq()], comparators=[Constant(value='BGR')])), Return(value=Call(func=Attribute(value=Name(id='input', ctx=Load()), attr='flip', ctx=Load()), args=[Constant(value=1)], keywords=[]))], decorator_list=[]), FunctionDef(name='forwardjwhPh', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='input')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\x9c ')), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_adjust_colorspace', ctx=Load()), args=[Name(id='input', ctx=Load())], keywords=[])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='features', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), Return(value=Name(id='x', ctx=Load()))], decorator_list=[])], decorator_list=[]), ClassDef(name='VGGaVIvI', bases=[Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Module', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Ȍ ś     Ȳų@ÑƗÉƭͥ     ˚ ǜ  ɸ ;  ųF *Ą')), FunctionDef(name='inp', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Constant(value=28))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='cha', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_channels', ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='std', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=List(elts=[Constant(value=1.0), Constant(value=1.0), Constant(value=1.0)], ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())]), FunctionDef(name='forwardjwhPh', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='input')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='   π       ɔ ǈ β  ')), Return(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='get_embedding', ctx=Load()), args=[Name(id='input', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='name'), arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=False)]), body=[Expr(value=Constant(value='\xad  ϡ ʜ͖    Ʀ  Č  ŭ ')), Expr(value=Call(func=Attribute(value=Call(func=Name(id='supe', ctx=Load()), args=[Name(id='VGGaVIvI', ctx=Load()), Name(id='self', ctx=Load())], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), If(test=Name(id='pretrained', ctx=Load()), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Pretrained weights are not available for VGG model.')], keywords=[]))], orelse=[]), If(test=Compare(left=Name(id='name', ctx=Load()), ops=[Eq()], comparators=[Constant(value='M3')]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Store())], value=Call(func=Name(id='ModelM3', ctx=Load()), args=[], keywords=[]))], orelse=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[JoinedStr(values=[Constant(value='Model name '), FormattedValue(value=Name(id='name', ctx=Load()), conversion=-1), Constant(value=' is not available for VGG models.')])], keywords=[]))]), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_channels', ctx=Store())], value=Attribute(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='conv10', ctx=Load()), attr='out_channels', ctx=Load())), Assign(targets=[Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='global_pool', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Identity', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_model', ctx=Load()), attr='last_linear', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Identity', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), FunctionDef(name='mean', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=List(elts=[Constant(value=0.5), Constant(value=0.5), Constant(value=0.5)], ctx=Load()))], decorator_list=[Name(id='propert', ctx=Load())])], decorator_list=[]), ClassDef(name='cgdmodel', bases=[Name(id='PMModel', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='       țķ    ɣ ')), FunctionDef(name='_get_model_', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='name'), arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Call(func=Call(func=Name(id='getattr', ctx=Load()), args=[Name(id='cgd', ctx=Load()), Name(id='name', ctx=Load())], keywords=[]), args=[], keywords=[keyword(arg='num_classes', value=Constant(value=1000)), keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))]))], decorator_list=[])], decorator_list=[]), ClassDef(name='pamodel', bases=[Name(id='PMModel', ctx=Load())], keywords=[], body=[FunctionDef(name='_get_model_', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='name'), arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='  ɿ  ÷͔ƹ τ   ')), If(test=Compare(left=Name(id='name', ctx=Load()), ops=[NotEq()], comparators=[Constant(value='bn_inception_simple')]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Call(func=Attribute(value=Constant(value='Unknown model {}.'), attr='format', ctx=Load()), args=[Name(id='name', ctx=Load())], keywords=[])], keywords=[]))], orelse=[]), Return(value=Call(func=Call(func=Name(id='getattr', ctx=Load()), args=[Name(id='bn_inception_simple', ctx=Load()), Name(id='name', ctx=Load())], keywords=[]), args=[], keywords=[keyword(arg='pretrained', value=Call(func=Name(id='bool', ctx=Load()), args=[Name(id='pretrained', ctx=Load())], keywords=[]))]))], decorator_list=[])], decorator_list=[])], type_ignores=[])