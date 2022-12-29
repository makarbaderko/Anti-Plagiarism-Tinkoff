Module(body=[ImportFrom(module='collections', names=[alias(name='OrderedDict')], level=0), Import(names=[alias(name='torch')]), ImportFrom(module='config', names=[alias(name='prepare_config')], level=2), ClassDef(name='StepSchedul_er', bases=[Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='optim', ctx=Load()), attr='lr_scheduler', ctx=Load()), attr='StepLR', ctx=Load())], keywords=[], body=[FunctionDef(name='get_default_config', args=arguments(posonlyargs=[], args=[arg(arg='step'), arg(arg='ga_mma')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=10), Constant(value=0.1)]), body=[Expr(value=Constant(value='\x92ʏ̷ĉGȌet¡ǥɄ³ȑ schedulϱer pǍaϥrĭametersɆ.Gʡɝ')), Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='step'), Name(id='step', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='gamma'), Name(id='ga_mma', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='sel_f'), arg(arg='optimizer'), arg(arg='num_ep')], kwonlyargs=[arg(arg='minimize_metricXL'), arg(arg='config')], kw_defaults=[Constant(value=True), Constant(value=None)], defaults=[]), body=[Assign(targets=[Name(id='config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='sel_f', ctx=Load()), Name(id='config', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='optimizer', ctx=Load())], keywords=[keyword(arg='step_size', value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='step'), ctx=Load())), keyword(arg='gamma', value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='gamma'), ctx=Load()))]))], decorator_list=[])], decorator_list=[]), ClassDef(name='MultiStepSch', bases=[Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='optim', ctx=Load()), attr='lr_scheduler', ctx=Load()), attr='MultiStepLR', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Configuͻrable LʟR scheduler.ΰ')), FunctionDef(name='get_default_config', args=arguments(posonlyargs=[], args=[arg(arg='milestones'), arg(arg='ga_mma')], kwonlyargs=[], kw_defaults=[], defaults=[List(elts=[Constant(value=9), Constant(value=14)], ctx=Load()), Constant(value=0.1)]), body=[Expr(value=Constant(value='Get scheȅduleɿ5rǺ pʄaramet\u0382ers.')), Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='milestones'), Name(id='milestones', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='gamma'), Name(id='ga_mma', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='sel_f'), arg(arg='optimizer'), arg(arg='num_ep')], kwonlyargs=[arg(arg='minimize_metricXL'), arg(arg='config')], kw_defaults=[Constant(value=True), Constant(value=None)], defaults=[]), body=[Assign(targets=[Name(id='config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='sel_f', ctx=Load()), Name(id='config', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='optimizer', ctx=Load())], keywords=[keyword(arg='milestones', value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='milestones'), ctx=Load())), keyword(arg='gamma', value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='gamma'), ctx=Load()))]))], decorator_list=[])], decorator_list=[]), ClassDef(name='PlateauScheduler', bases=[Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='optim', ctx=Load()), attr='lr_scheduler', ctx=Load()), attr='ReduceLROnPlateau', ctx=Load())], keywords=[], body=[FunctionDef(name='get_default_config', args=arguments(posonlyargs=[], args=[arg(arg='patience_'), arg(arg='factor')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=10), Constant(value=0.1)]), body=[Expr(value=Constant(value='¸Get scfhεeɔd;ulʎer parametŵers.')), Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='patience'), Name(id='patience_', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='factor'), Name(id='factor', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='sel_f'), arg(arg='optimizer'), arg(arg='num_ep')], kwonlyargs=[arg(arg='minimize_metricXL'), arg(arg='config')], kw_defaults=[Constant(value=True), Constant(value=None)], defaults=[]), body=[Expr(value=Constant(value=' Ųʙ: \x9c                Γ ͣ    \xad    \x93     ')), Assign(targets=[Name(id='config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='sel_f', ctx=Load()), Name(id='config', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='optimizer', ctx=Load())], keywords=[keyword(arg='mode', value=IfExp(test=Name(id='minimize_metricXL', ctx=Load()), body=Constant(value='min'), orelse=Constant(value='max'))), keyword(arg='patience', value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='patience'), ctx=Load())), keyword(arg='factor', value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='factor'), ctx=Load()))]))], decorator_list=[])], decorator_list=[]), ClassDef(name='WarmupScheduler', bases=[Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='optim', ctx=Load()), attr='lr_scheduler', ctx=Load()), attr='_LRScheduler', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='ßϫAdǱˡd w\x82armΑʄupȮ§ stŐþeȼůps¥ to LĤRǚɼ scheĮdőuül\x9eeWrœ.')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='sel_f'), arg(arg='s'), arg(arg='WARMUP_EPOCHS')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=1)]), body=[Expr(value=Constant(value='ϕǛ    ƥ    ')), Assign(targets=[Attribute(value=Name(id='sel_f', ctx=Load()), attr='_scheduler', ctx=Store())], value=Name(id='s', ctx=Load())), Assign(targets=[Attribute(value=Name(id='sel_f', ctx=Load()), attr='_warmup_epochs', ctx=Store())], value=Name(id='WARMUP_EPOCHS', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='optimizer', value=Attribute(value=Name(id='s', ctx=Load()), attr='optimizer', ctx=Load())), keyword(arg='last_epoch', value=Attribute(value=Name(id='s', ctx=Load()), attr='last_epoch', ctx=Load())), keyword(arg='verbose', value=Attribute(value=Name(id='s', ctx=Load()), attr='verbose', ctx=Load()))]))], decorator_list=[]), FunctionDef(name='state_dict', args=arguments(posonlyargs=[], args=[arg(arg='sel_f')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' Ͷ    Ǐ    Ȥ ʗ ÄŤ     ɭ ǔ         ȧǼ')), Assign(targets=[Name(id='state', ctx=Store())], value=IfExp(test=Compare(left=Attribute(value=Name(id='sel_f', ctx=Load()), attr='_scheduler', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=Call(func=Attribute(value=Attribute(value=Name(id='sel_f', ctx=Load()), attr='_scheduler', ctx=Load()), attr='state_dict', ctx=Load()), args=[], keywords=[]), orelse=Dict(keys=[], values=[]))), Assign(targets=[Subscript(value=Name(id='state', ctx=Load()), slice=Constant(value='warmup_epochs'), ctx=Store())], value=Attribute(value=Name(id='sel_f', ctx=Load()), attr='_warmup_epochs', ctx=Load())), Return(value=Name(id='state', ctx=Load()))], decorator_list=[]), FunctionDef(name='step', args=arguments(posonlyargs=[], args=[arg(arg='sel_f')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Attribute(value=Name(id='sel_f', ctx=Load()), attr='last_epoch', ctx=Load()), ops=[Gt()], comparators=[Constant(value=0)]), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='sel_f', ctx=Load()), attr='_scheduler', ctx=Load()), attr='step', ctx=Load()), args=[], keywords=[]))], orelse=[]), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='step', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), FunctionDef(name='get_', args=arguments(posonlyargs=[], args=[arg(arg='sel_f')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='lr', ctx=Store())], value=IfExp(test=Compare(left=Attribute(value=Name(id='sel_f', ctx=Load()), attr='_scheduler', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=Call(func=Attribute(value=Attribute(value=Name(id='sel_f', ctx=Load()), attr='_scheduler', ctx=Load()), attr='get_last_lr', ctx=Load()), args=[], keywords=[]), orelse=Attribute(value=Name(id='sel_f', ctx=Load()), attr='base_lrs', ctx=Load()))), If(test=Compare(left=Attribute(value=Name(id='sel_f', ctx=Load()), attr='last_epoch', ctx=Load()), ops=[LtE()], comparators=[Attribute(value=Name(id='sel_f', ctx=Load()), attr='_warmup_epochs', ctx=Load())]), body=[Assign(targets=[Name(id='lr', ctx=Store())], value=BinOp(left=List(elts=[Constant(value=0.0)], ctx=Load()), op=Mult(), right=Call(func=Name(id='len', ctx=Load()), args=[Name(id='lr', ctx=Load())], keywords=[])))], orelse=[If(test=Compare(left=Attribute(value=Name(id='sel_f', ctx=Load()), attr='last_epoch', ctx=Load()), ops=[Eq()], comparators=[BinOp(left=Attribute(value=Name(id='sel_f', ctx=Load()), attr='_warmup_epochs', ctx=Load()), op=Add(), right=Constant(value=1))]), body=[Assign(targets=[Name(id='lr', ctx=Store())], value=Attribute(value=Name(id='sel_f', ctx=Load()), attr='base_lrs', ctx=Load()))], orelse=[])]), Return(value=Name(id='lr', ctx=Load()))], decorator_list=[]), FunctionDef(name='load_state_dict', args=arguments(posonlyargs=[], args=[arg(arg='sel_f'), arg(arg='state_dict')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='state_dict', ctx=Store())], value=Call(func=Attribute(value=Name(id='state_dict', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='sel_f', ctx=Load()), attr='_warmup_epochs', ctx=Store())], value=Call(func=Attribute(value=Name(id='state_dict', ctx=Load()), attr='pop', ctx=Load()), args=[Constant(value='warmup_epochs')], keywords=[])), If(test=Compare(left=Attribute(value=Name(id='sel_f', ctx=Load()), attr='_scheduler', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='sel_f', ctx=Load()), attr='_scheduler', ctx=Load()), attr='load_state_dict', ctx=Load()), args=[Name(id='state_dict', ctx=Load())], keywords=[]))], orelse=[]), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='load_state_dict', ctx=Load()), args=[Name(id='state_dict', ctx=Load())], keywords=[]))], decorator_list=[])], decorator_list=[]), ClassDef(name='ExponentialScheduler', bases=[Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='optim', ctx=Load()), attr='lr_scheduler', ctx=Load()), attr='ExponentialLR', ctx=Load())], keywords=[], body=[FunctionDef(name='get_default_config', args=arguments(posonlyargs=[], args=[arg(arg='lr_at_last_epochIC')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=0.0001)]), body=[Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='lr_at_last_epoch'), Name(id='lr_at_last_epochIC', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='sel_f'), arg(arg='optimizer'), arg(arg='num_ep')], kwonlyargs=[arg(arg='minimize_metricXL'), arg(arg='config')], kw_defaults=[Constant(value=True), Constant(value=None)], defaults=[]), body=[Expr(value=Constant(value=' ʣ οϯ     Ͱ     κû Lȅ\x88ˤ9Ç \x9c             ʎ    ]')), Assign(targets=[Name(id='config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='sel_f', ctx=Load()), Name(id='config', ctx=Load())], keywords=[])), Assign(targets=[Name(id='lr_0', ctx=Store())], value=Subscript(value=Subscript(value=Attribute(value=Name(id='optimizer', ctx=Load()), attr='param_groups', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value='lr'), ctx=Load())), Assign(targets=[Name(id='lr_', ctx=Store())], value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='lr_at_last_epoch'), ctx=Load())), Assign(targets=[Name(id='t', ctx=Store())], value=Name(id='num_ep', ctx=Load())), Assign(targets=[Name(id='ga_mma', ctx=Store())], value=BinOp(left=BinOp(left=Name(id='lr_', ctx=Load()), op=Div(), right=Name(id='lr_0', ctx=Load())), op=Pow(), right=BinOp(left=Constant(value=1), op=Div(), right=Name(id='t', ctx=Load())))), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='optimizer', ctx=Load())], keywords=[keyword(arg='gamma', value=Name(id='ga_mma', ctx=Load()))]))], decorator_list=[])], decorator_list=[])], type_ignores=[])