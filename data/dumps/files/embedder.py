Module(body=[ImportFrom(module='collections', names=[alias(name='OrderedDict')], level=0), Import(names=[alias(name='torch')]), ImportFrom(module='config', names=[alias(name='prepare_config')], level=3), ImportFrom(module='torch', names=[alias(name='disable_amp'), alias(name='freeze'), alias(name='freeze_bn'), alias(name='eval_bn')], level=3), ImportFrom(module='cnn', names=[alias(name='ResNetModel'), alias(name='CotrainingModel'), alias(name='EfficientNet'), alias(name='PyramidNet'), alias(name='PMModel'), alias(name='CGDModel'), alias(name='PAModel'), alias(name='VGG'), alias(name='TorchVGGModel')], level=1), ImportFrom(module='pooling', names=[alias(name='MultiPool2d')], level=1), ClassDef(name='SequentialFP32', bases=[Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Sequential', ctx=Load())], keywords=[], body=[FunctionDef(name='forward', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='input')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[With(items=[withitem(context_expr=Call(func=Name(id='disable_amp', ctx=Load()), args=[], keywords=[]))], body=[Return(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='forward', ctx=Load()), args=[Call(func=Attribute(value=Name(id='input', ctx=Load()), attr='float', ctx=Load()), args=[], keywords=[])], keywords=[]))])], decorator_list=[])], decorator_list=[]), ClassDef(name='IdentityEmbedder', bases=[Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Module', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Pass input embeddings to the output.')), FunctionDef(name='get_default_config', args=arguments(posonlyargs=[], args=[arg(arg='head_normalize')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True)]), body=[Expr(value=Constant(value='Get embedder parameters.')), Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='head_normalize'), Name(id='head_normalize', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='out_features')], kwonlyargs=[arg(arg='normalizer'), arg(arg='config')], kw_defaults=[Constant(value=None), Constant(value=None)], defaults=[]), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='self', ctx=Load()), Name(id='config', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_out_features', ctx=Store())], value=Name(id='out_features', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_normalizer', ctx=Store())], value=IfExp(test=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='head_normalize'), ctx=Load()), body=Name(id='normalizer', ctx=Load()), orelse=Constant(value=None)))], decorator_list=[]), FunctionDef(name='input_size', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Pretrained model input image size.')), Raise(exc=Call(func=Name(id='NotImplementedError', ctx=Load()), args=[Constant(value='Input size is unavailable for identity embedder.')], keywords=[]))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='in_channels', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Raise(exc=Call(func=Name(id='NotImplementedError', ctx=Load()), args=[Constant(value='Input channels are unavailable for identity embedder.')], keywords=[]))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='forward', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='embeddings')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Subscript(value=Attribute(value=Name(id='embeddings', ctx=Load()), attr='shape', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=1)), ctx=Load()), ops=[NotEq()], comparators=[Attribute(value=Name(id='self', ctx=Load()), attr='_out_features', ctx=Load())]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Call(func=Attribute(value=Constant(value='Expected embeddings with dimension {}, got {}'), attr='format', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_out_features', ctx=Load()), Subscript(value=Attribute(value=Name(id='embeddings', ctx=Load()), attr='shape', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=1)), ctx=Load())], keywords=[])], keywords=[]))], orelse=[]), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_normalizer', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='embeddings', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_normalizer', ctx=Load()), args=[Name(id='embeddings', ctx=Load())], keywords=[]))], orelse=[]), Return(value=Name(id='embeddings', ctx=Load()))], decorator_list=[])], decorator_list=[]), ClassDef(name='CNNEmbedder', bases=[Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Module', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Model to map input images to embeddings.\n\n    Embedder computation pipeline:\n    1. Stem (CNN model).\n    2. Pooling (CNN output spatial aggregation method).\n    3. Head (mapping from CNN output to embedding).\n    3*. Extra head for uncertainty prediction.\n    4. Normalizer (batchnorm of embeddings for some models).\n    ')), Assign(targets=[Name(id='MODELS', ctx=Store())], value=Dict(keys=[Constant(value='resnet18'), Constant(value='resnet34'), Constant(value='resnet50'), Constant(value='resnet101'), Constant(value='wide_resnet16_8'), Constant(value='wide_resnet50_2'), Constant(value='wide_resnet101_2'), Constant(value='wide_resnet28_10'), Constant(value='efficientnet_v2_s'), Constant(value='efficientnet_v2_m'), Constant(value='efficientnet_v2_l'), Constant(value='pyramidnet272'), Constant(value='bninception'), Constant(value='bninception_simple'), Constant(value='se_resnet50'), Constant(value='cgd_se_resnet50'), Constant(value='vgg_m3'), Constant(value='vgg19')], values=[Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='ResNetModel', ctx=Load()), args=[Constant(value='resnet18')], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='ResNetModel', ctx=Load()), args=[Constant(value='resnet34')], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='ResNetModel', ctx=Load()), args=[Constant(value='resnet50')], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='ResNetModel', ctx=Load()), args=[Constant(value='resnet101')], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='CotrainingModel', ctx=Load()), args=[Constant(value='wide_resnet16_8')], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='ResNetModel', ctx=Load()), args=[Constant(value='wide_resnet50_2')], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='ResNetModel', ctx=Load()), args=[Constant(value='wide_resnet101_2')], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='CotrainingModel', ctx=Load()), args=[Constant(value='wide_resnet28_10')], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='EfficientNet', ctx=Load()), args=[Constant(value='efficientnet_v2_s')], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='EfficientNet', ctx=Load()), args=[Constant(value='efficientnet_v2_m')], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='EfficientNet', ctx=Load()), args=[Constant(value='efficientnet_v2_l')], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='PyramidNet', ctx=Load()), args=[Constant(value='cifar10')], keywords=[keyword(arg='depth', value=Constant(value=272)), keyword(arg='alpha', value=Constant(value=200)), keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='PMModel', ctx=Load()), args=[Constant(value='bninception')], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='PAModel', ctx=Load()), args=[Constant(value='bn_inception_simple')], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='PMModel', ctx=Load()), args=[Constant(value='se_resnet50')], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='CGDModel', ctx=Load()), args=[Constant(value='cgd_se_resnet50')], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='VGG', ctx=Load()), args=[Constant(value='M3')], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='pretrained')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='TorchVGGModel', ctx=Load()), args=[Constant(value='vgg19')], keywords=[keyword(arg='pretrained', value=Name(id='pretrained', ctx=Load()))]))])), Assign(targets=[Name(id='POOLINGS', ctx=Store())], value=Dict(keys=[Constant(value='avg'), Constant(value='max'), Constant(value='multi')], values=[Lambda(args=arguments(posonlyargs=[], args=[arg(arg='config')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='AdaptiveAvgPool2d', ctx=Load()), args=[], keywords=[keyword(arg='output_size', value=Tuple(elts=[Constant(value=1), Constant(value=1)], ctx=Load())), keyword(value=BoolOp(op=Or(), values=[Name(id='config', ctx=Load()), Dict(keys=[], values=[])]))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='config')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='AdaptiveMaxPool2d', ctx=Load()), args=[], keywords=[keyword(arg='output_size', value=Tuple(elts=[Constant(value=1), Constant(value=1)], ctx=Load())), keyword(value=BoolOp(op=Or(), values=[Name(id='config', ctx=Load()), Dict(keys=[], values=[])]))])), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='config')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='MultiPool2d', ctx=Load()), args=[], keywords=[keyword(value=BoolOp(op=Or(), values=[Name(id='config', ctx=Load()), Dict(keys=[], values=[])]))]))])), FunctionDef(name='get_default_config', args=arguments(posonlyargs=[], args=[arg(arg='model_type'), arg(arg='pretrained'), arg(arg='freeze_bn'), arg(arg='pooling_type'), arg(arg='pooling_params'), arg(arg='dropout'), arg(arg='head_batchnorm'), arg(arg='head_normalize'), arg(arg='extra_head_dim'), arg(arg='extra_head_layers'), arg(arg='freeze_stem'), arg(arg='freeze_head'), arg(arg='freeze_extra_head'), arg(arg='freeze_normalizer'), arg(arg='output_scale'), arg(arg='disable_head')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value='resnet50'), Constant(value=False), Constant(value=False), Constant(value='avg'), Constant(value=None), Constant(value=0.0), Constant(value=True), Constant(value=True), Constant(value=0), Constant(value=3), Constant(value=False), Constant(value=False), Constant(value=False), Constant(value=False), Constant(value=1.0), Constant(value=False)]), body=[Expr(value=Constant(value='Get embedder parameters.\n\n        Args:\n            model_type: One of "resnet18", "resnet34", "resnet50", "resnet101", "bninception", "se_resnet50" and "cgd_se_resnet50".\n            pretrained: Whether to use ImageNet-pretrained model or start from scratch.\n            freeze_bn: Whether to freez batch normalization or not.\n            pooling_type: Type of pooling ("avg", "max" or "multi").\n            pooling_params: Parameters of the pooling.\n            dropout: Head dropout probability during training.\n            head_batchnorm: Whether to apply 1-D batchnorm to CNN output or not.\n            head_normalize: Whether to apply provided normalizer or not.\n            extra_head_dim: Use additional head (usually for distribution concentration estimation).\n                Output embedding is concatenation of the main and extra heads.\n            extra_head_layers: The number of FC layers in extra head.\n            freeze_stem: Freeze stem during training.\n            freeze_head: Freeze main head during training.\n            freeze_extra_head: Freeze extra head during training.\n            freeze_normalizer: Freeze normalizer during training.\n            output_scale: Output embedding multiplier (used in vMF-loss).\n            disable_head: Whether to disable head layers.\n        ')), Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='model_type'), Name(id='model_type', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='pretrained'), Name(id='pretrained', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='freeze_bn'), Name(id='freeze_bn', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='pooling_type'), Name(id='pooling_type', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='pooling_params'), Name(id='pooling_params', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='dropout'), Name(id='dropout', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='head_batchnorm'), Name(id='head_batchnorm', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='head_normalize'), Name(id='head_normalize', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='extra_head_dim'), Name(id='extra_head_dim', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='extra_head_layers'), Name(id='extra_head_layers', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='freeze_stem'), Name(id='freeze_stem', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='freeze_head'), Name(id='freeze_head', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='freeze_extra_head'), Name(id='freeze_extra_head', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='freeze_normalizer'), Name(id='freeze_normalizer', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='output_scale'), Name(id='output_scale', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='disable_head'), Name(id='disable_head', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='out_features')], kwonlyargs=[arg(arg='normalizer'), arg(arg='config')], kw_defaults=[Constant(value=None), Constant(value=None)], defaults=[]), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='self', ctx=Load()), Name(id='config', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_stem', ctx=Store())], value=Call(func=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='MODELS', ctx=Load()), slice=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='model_type'), ctx=Load()), ctx=Load()), args=[], keywords=[keyword(arg='pretrained', value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='pretrained'), ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_pooling', ctx=Store())], value=Call(func=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='POOLINGS', ctx=Load()), slice=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='pooling_type'), ctx=Load()), ctx=Load()), args=[], keywords=[keyword(arg='config', value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='pooling_params'), ctx=Load()))])), Assign(targets=[Name(id='pooling_broadcast', ctx=Store())], value=IfExp(test=Call(func=Name(id='hasattr', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_pooling', ctx=Load()), Constant(value='channels_multiplier')], keywords=[]), body=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_pooling', ctx=Load()), attr='channels_multiplier', ctx=Load()), orelse=Constant(value=1))), If(test=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='disable_head'), ctx=Load()), body=[Assign(targets=[Name(id='actual_out_features', ctx=Store())], value=BinOp(left=BinOp(left=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_stem', ctx=Load()), attr='channels', ctx=Load()), op=Mult(), right=Name(id='pooling_broadcast', ctx=Load())), op=Add(), right=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='extra_head_dim'), ctx=Load()))), If(test=Compare(left=Name(id='out_features', ctx=Load()), ops=[NotEq()], comparators=[Name(id='actual_out_features', ctx=Load())]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[JoinedStr(values=[Constant(value='Expected number of output dimensions ('), FormattedValue(value=Name(id='out_features', ctx=Load()), conversion=-1), Constant(value=") doesn't match the actual number ("), FormattedValue(value=Name(id='actual_out_features', ctx=Load()), conversion=-1), Constant(value=') when `disable_head=True`.')])], keywords=[]))], orelse=[])], orelse=[]), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_head', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_make_head', ctx=Load()), args=[BinOp(left=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_stem', ctx=Load()), attr='channels', ctx=Load()), op=Mult(), right=Name(id='pooling_broadcast', ctx=Load())), BinOp(left=Name(id='out_features', ctx=Load()), op=Sub(), right=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='extra_head_dim'), ctx=Load()))], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_extra_head', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_make_extra_head', ctx=Load()), args=[BinOp(left=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_stem', ctx=Load()), attr='channels', ctx=Load()), op=Mult(), right=Name(id='pooling_broadcast', ctx=Load())), Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='extra_head_dim'), ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_normalizer', ctx=Store())], value=IfExp(test=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='head_normalize'), ctx=Load()), body=Name(id='normalizer', ctx=Load()), orelse=Constant(value=None))), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='output_scale', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='output_scale'), ctx=Load())), If(test=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='freeze_bn'), ctx=Load()), body=[Expr(value=Call(func=Name(id='freeze_bn', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_stem', ctx=Load())], keywords=[]))], orelse=[]), If(test=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='freeze_stem'), ctx=Load()), body=[Expr(value=Call(func=Name(id='freeze', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_stem', ctx=Load())], keywords=[]))], orelse=[]), If(test=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='freeze_head'), ctx=Load()), body=[Expr(value=Call(func=Name(id='freeze', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_head', ctx=Load())], keywords=[]))], orelse=[]), If(test=BoolOp(op=And(), values=[Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='freeze_extra_head'), ctx=Load()), Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_extra_head', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)])]), body=[Expr(value=Call(func=Name(id='freeze', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_extra_head', ctx=Load())], keywords=[]))], orelse=[]), If(test=BoolOp(op=And(), values=[Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='freeze_normalizer'), ctx=Load()), Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_normalizer', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)])]), body=[Expr(value=Call(func=Name(id='freeze', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_normalizer', ctx=Load())], keywords=[]))], orelse=[])], decorator_list=[]), FunctionDef(name='input_size', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Pretrained model input image size.')), Return(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_stem', ctx=Load()), attr='input_size', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='in_channels', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Constant(value=3))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='mean', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Pretrained model input normalization mean.')), Return(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_stem', ctx=Load()), attr='mean', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='std', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Pretrained model input normalization STD.')), Return(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_stem', ctx=Load()), attr='std', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='output_scale', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=BoolOp(op=Or(), values=[UnaryOp(op=Not(), operand=Call(func=Name(id='hasattr', ctx=Load()), args=[Name(id='self', ctx=Load()), Constant(value='_output_scale')], keywords=[])), Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_output_scale', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)])]), body=[Return(value=Constant(value=None))], orelse=[]), Return(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_output_scale', ctx=Load()), attr='item', ctx=Load()), args=[], keywords=[]))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='output_scale', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='scale')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Set main head output scale.')), If(test=Call(func=Name(id='hasattr', ctx=Load()), args=[Name(id='self', ctx=Load()), Constant(value='_output_scale')], keywords=[]), body=[Delete(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_output_scale', ctx=Del())])], orelse=[]), If(test=Compare(left=Name(id='scale', ctx=Load()), ops=[NotEq()], comparators=[Constant(value=1.0)]), body=[Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='register_buffer', ctx=Load()), args=[Constant(value='_output_scale'), Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='full', ctx=Load()), args=[List(elts=[], ctx=Load()), Name(id='scale', ctx=Load())], keywords=[])], keywords=[]))], orelse=[])], decorator_list=[Attribute(value=Name(id='output_scale', ctx=Load()), attr='setter', ctx=Load())]), FunctionDef(name='forward', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='images')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='cnn_output', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_stem', ctx=Load()), args=[Name(id='images', ctx=Load())], keywords=[])), Assign(targets=[Name(id='cnn_output', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_pooling', ctx=Load()), args=[Name(id='cnn_output', ctx=Load())], keywords=[])), Assign(targets=[Name(id='cnn_output', ctx=Store())], value=Call(func=Attribute(value=Name(id='cnn_output', ctx=Load()), attr='flatten', ctx=Load()), args=[Constant(value=1)], keywords=[])), Assign(targets=[Name(id='head_output', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_head', ctx=Load()), args=[Name(id='cnn_output', ctx=Load())], keywords=[])), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='output_scale', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='head_output', ctx=Store())], value=BinOp(left=Name(id='head_output', ctx=Load()), op=Mult(), right=Attribute(value=Name(id='self', ctx=Load()), attr='output_scale', ctx=Load())))], orelse=[]), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_extra_head', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='extra_head_output', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_extra_head', ctx=Load()), args=[Name(id='cnn_output', ctx=Load())], keywords=[])), Assign(targets=[Name(id='head_output', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='cat', ctx=Load()), args=[List(elts=[Name(id='head_output', ctx=Load()), Name(id='extra_head_output', ctx=Load())], ctx=Load())], keywords=[keyword(arg='dim', value=UnaryOp(op=USub(), operand=Constant(value=1)))]))], orelse=[]), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_normalizer', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='head_output', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_normalizer', ctx=Load()), args=[Name(id='head_output', ctx=Load())], keywords=[]))], orelse=[]), Return(value=Name(id='head_output', ctx=Load()))], decorator_list=[]), FunctionDef(name='train', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='mode')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='train', ctx=Load()), args=[Name(id='mode', ctx=Load())], keywords=[])), If(test=BoolOp(op=Or(), values=[Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='freeze_bn'), ctx=Load()), Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='freeze_stem'), ctx=Load())]), body=[Expr(value=Call(func=Name(id='eval_bn', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_stem', ctx=Load())], keywords=[]))], orelse=[]), If(test=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='freeze_head'), ctx=Load()), body=[Expr(value=Call(func=Name(id='eval_bn', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_head', ctx=Load())], keywords=[]))], orelse=[]), If(test=BoolOp(op=And(), values=[Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='freeze_extra_head'), ctx=Load()), Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_extra_head', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)])]), body=[Expr(value=Call(func=Name(id='eval_bn', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_extra_head', ctx=Load())], keywords=[]))], orelse=[]), If(test=BoolOp(op=And(), values=[Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='freeze_normalizer'), ctx=Load()), Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_normalizer', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)])]), body=[Expr(value=Call(func=Name(id='eval_bn', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_normalizer', ctx=Load())], keywords=[]))], orelse=[])], decorator_list=[]), FunctionDef(name='_make_head', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='in_features'), arg(arg='out_features')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='head_layers', ctx=Store())], value=List(elts=[], ctx=Load())), If(test=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='head_batchnorm'), ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Name(id='head_layers', ctx=Load()), attr='append', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='BatchNorm1d', ctx=Load()), args=[Name(id='in_features', ctx=Load())], keywords=[])], keywords=[]))], orelse=[]), If(test=Compare(left=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='dropout'), ctx=Load()), ops=[Gt()], comparators=[Constant(value=0)]), body=[Expr(value=Call(func=Attribute(value=Name(id='head_layers', ctx=Load()), attr='append', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Dropout', ctx=Load()), args=[Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='dropout'), ctx=Load())], keywords=[])], keywords=[]))], orelse=[]), If(test=UnaryOp(op=Not(), operand=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='disable_head'), ctx=Load())), body=[Expr(value=Call(func=Attribute(value=Name(id='head_layers', ctx=Load()), attr='append', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Linear', ctx=Load()), args=[Name(id='in_features', ctx=Load()), Name(id='out_features', ctx=Load())], keywords=[])], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='init', ctx=Load()), attr='constant_', ctx=Load()), args=[Attribute(value=Subscript(value=Name(id='head_layers', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=1)), ctx=Load()), attr='bias', ctx=Load()), Constant(value=0)], keywords=[]))], orelse=[]), Return(value=Call(func=Name(id='SequentialFP32', ctx=Load()), args=[Starred(value=Name(id='head_layers', ctx=Load()), ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='_make_extra_head', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='in_features'), arg(arg='out_features')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Name(id='out_features', ctx=Load()), ops=[Eq()], comparators=[Constant(value=0)]), body=[Return(value=Constant(value=None))], orelse=[]), Assign(targets=[Name(id='head_layers', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Name(id='_', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[BinOp(left=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='extra_head_layers'), ctx=Load()), op=Sub(), right=Constant(value=1))], keywords=[]), body=[Expr(value=Call(func=Attribute(value=Name(id='head_layers', ctx=Load()), attr='append', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Linear', ctx=Load()), args=[Name(id='in_features', ctx=Load()), BinOp(left=Name(id='in_features', ctx=Load()), op=FloorDiv(), right=Constant(value=2))], keywords=[])], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='ReLU', ctx=Load()), args=[], keywords=[keyword(arg='inplace', value=Constant(value=True))])), AugAssign(target=Name(id='in_features', ctx=Store()), op=FloorDiv(), value=Constant(value=2))], orelse=[]), Expr(value=Call(func=Attribute(value=Name(id='head_layers', ctx=Load()), attr='append', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='Linear', ctx=Load()), args=[Name(id='in_features', ctx=Load()), Name(id='out_features', ctx=Load())], keywords=[])], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='init', ctx=Load()), attr='constant_', ctx=Load()), args=[Attribute(value=Subscript(value=Name(id='head_layers', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=1)), ctx=Load()), attr='bias', ctx=Load()), Constant(value=0)], keywords=[])), Return(value=Call(func=Name(id='SequentialFP32', ctx=Load()), args=[Starred(value=Name(id='head_layers', ctx=Load()), ctx=Load())], keywords=[]))], decorator_list=[])], decorator_list=[])], type_ignores=[])