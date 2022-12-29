Module(body=[Import(names=[alias(name='torch')]), Import(names=[alias(name='torch.nn.functional', asname='F')]), Import(names=[alias(name='wandb')]), Import(names=[alias(name='catalyst.callbacks.checkpoint')]), ImportFrom(module='catalyst', names=[alias(name='dl')], level=0), ImportFrom(module='catalyst.loggers.wandb', names=[alias(name='WandbLogger')], level=0), ImportFrom(module='catalyst.callbacks.control_flow', names=[alias(name='LOADERS')], level=0), ClassDef(name='_filter_fn_from_loaders', bases=[], keywords=[], body=[FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='loaders', annotation=Name(id='LOADERS', ctx=Load())), arg(arg='reverse_condition', annotation=Name(id='bool', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assert(test=Compare(left=Name(id='reverse_condition', ctx=Load()), ops=[Is()], comparators=[Constant(value=False)])), Assert(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='loaders', ctx=Load()), Name(id='str', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_loader', ctx=Store())], value=Name(id='loaders', ctx=Load()))], decorator_list=[]), FunctionDef(name='__call__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='stage'), arg(arg='epoch'), arg(arg='loader')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Compare(left=Name(id='loader', ctx=Load()), ops=[Eq()], comparators=[Attribute(value=Name(id='self', ctx=Load()), attr='_loader', ctx=Load())]))], decorator_list=[])], decorator_list=[]), Assign(targets=[Attribute(value=Attribute(value=Attribute(value=Name(id='catalyst', ctx=Load()), attr='callbacks', ctx=Load()), attr='control_flow', ctx=Load()), attr='_filter_fn_from_loaders', ctx=Store())], value=Name(id='_filter_fn_from_loaders', ctx=Load())), ClassDef(name='AfterForkWandbLogger', bases=[Name(id='WandbLogger', ctx=Load())], keywords=[], body=[FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='project'), arg(arg='name'), arg(arg='entity')], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[Constant(value=None), Constant(value=None), Constant(value=None)]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='project', ctx=Store())], value=Name(id='project', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='name', ctx=Store())], value=Name(id='name', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='entity', ctx=Store())], value=Name(id='entity', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='run', ctx=Store())], value=Constant(value=None)), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='kwargs', ctx=Store())], value=Name(id='kwargs', ctx=Load()))], decorator_list=[]), FunctionDef(name='init', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='run', ctx=Store())], value=Call(func=Attribute(value=Name(id='wandb', ctx=Load()), attr='init', ctx=Load()), args=[], keywords=[keyword(arg='project', value=Attribute(value=Name(id='self', ctx=Load()), attr='project', ctx=Load())), keyword(arg='name', value=Attribute(value=Name(id='self', ctx=Load()), attr='name', ctx=Load())), keyword(arg='entity', value=Attribute(value=Name(id='self', ctx=Load()), attr='entity', ctx=Load())), keyword(arg='allow_val_change', value=Constant(value=True)), keyword(arg='tags', value=List(elts=[], ctx=Load())), keyword(value=Attribute(value=Name(id='self', ctx=Load()), attr='kwargs', ctx=Load()))]))], decorator_list=[]), FunctionDef(name='log_hparams', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='hparams'), arg(arg='scope', annotation=Name(id='str', ctx=Load())), arg(arg='run_key', annotation=Name(id='str', ctx=Load())), arg(arg='stage_key', annotation=Name(id='str', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None), Constant(value=None), Constant(value=None)]), body=[If(test=BoolOp(op=And(), values=[Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='run', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), Compare(left=Name(id='scope', ctx=Load()), ops=[Eq()], comparators=[Constant(value='stage')])]), body=[Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='init', ctx=Load()), args=[], keywords=[]))], orelse=[]), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='run', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='log_hparams', ctx=Load()), args=[Name(id='hparams', ctx=Load()), Name(id='scope', ctx=Load()), Name(id='run_key', ctx=Load()), Name(id='stage_key', ctx=Load())], keywords=[]))], orelse=[])], decorator_list=[], returns=Constant(value=None))], decorator_list=[]), ClassDef(name='ClosureOptimizer', bases=[], keywords=[], body=[FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='optimizer'), arg(arg='closure')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_optimizer', ctx=Store())], value=Name(id='optimizer', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_closure', ctx=Store())], value=Name(id='closure', ctx=Load()))], decorator_list=[]), FunctionDef(name='step', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_optimizer', ctx=Load()), attr='step', ctx=Load()), args=[], keywords=[keyword(arg='closure', value=Attribute(value=Name(id='self', ctx=Load()), attr='_closure', ctx=Load()))]))], decorator_list=[]), FunctionDef(name='param_groups', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_optimizer', ctx=Load()), attr='param_groups', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())])], decorator_list=[]), ClassDef(name='OptimizerCallback', bases=[Attribute(value=Name(id='dl', ctx=Load()), attr='OptimizerCallback', ctx=Load())], keywords=[], body=[FunctionDef(name='on_batch_end', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='runner')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Event handler.')), If(test=Attribute(value=Name(id='runner', ctx=Load()), attr='is_train_loader', ctx=Load()), body=[If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='accumulation_steps', ctx=Load()), ops=[NotEq()], comparators=[Constant(value=1)]), body=[Raise(exc=Call(func=Name(id='NotImplementedError', ctx=Load()), args=[Constant(value="Doesn't support closure with accumulation_steps.")], keywords=[]))], orelse=[]), AugAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='_accumulation_counter', ctx=Store()), op=Add(), value=Constant(value=1)), Assign(targets=[Name(id='need_gradient_step', ctx=Store())], value=Compare(left=BinOp(left=Attribute(value=Name(id='self', ctx=Load()), attr='_accumulation_counter', ctx=Load()), op=Mod(), right=Attribute(value=Name(id='self', ctx=Load()), attr='accumulation_steps', ctx=Load())), ops=[Eq()], comparators=[Constant(value=0)])), Assign(targets=[Name(id='loss', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='runner', ctx=Load()), attr='batch_metrics', ctx=Load()), slice=Attribute(value=Name(id='self', ctx=Load()), attr='metric_key', ctx=Load()), ctx=Load())), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='runner', ctx=Load()), attr='engine', ctx=Load()), attr='backward_loss', ctx=Load()), args=[Name(id='loss', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='optimizer', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_apply_gradnorm', ctx=Load()), args=[Name(id='runner', ctx=Load())], keywords=[])), If(test=Name(id='need_gradient_step', ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='runner', ctx=Load()), attr='engine', ctx=Load()), attr='optimizer_step', ctx=Load()), args=[Name(id='loss', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), Call(func=Name(id='ClosureOptimizer', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='optimizer', ctx=Load()), Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_closure', ctx=Load()), args=[Name(id='runner', ctx=Load())], keywords=[]))], keywords=[])], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='runner', ctx=Load()), attr='engine', ctx=Load()), attr='zero_grad', ctx=Load()), args=[Name(id='loss', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='optimizer', ctx=Load())], keywords=[]))], orelse=[]), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='runner', ctx=Load()), attr='batch_metrics', ctx=Load()), attr='update', ctx=Load()), args=[Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_lr_momentum_stats', ctx=Load()), args=[], keywords=[])], keywords=[])), If(test=Call(func=Name(id='hasattr', ctx=Load()), args=[Attribute(value=Name(id='runner', ctx=Load()), attr='engine', ctx=Load()), Constant(value='scaler')], keywords=[]), body=[Assign(targets=[Name(id='scaler_state', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Attribute(value=Name(id='runner', ctx=Load()), attr='engine', ctx=Load()), attr='scaler', ctx=Load()), attr='state_dict', ctx=Load()), args=[], keywords=[])), Assign(targets=[Subscript(value=Attribute(value=Name(id='runner', ctx=Load()), attr='batch_metrics', ctx=Load()), slice=Constant(value='gradient/scale'), ctx=Store())], value=BoolOp(op=Or(), values=[Subscript(value=Name(id='scaler_state', ctx=Load()), slice=Constant(value='scale'), ctx=Load()), Constant(value=1.0)])), Assign(targets=[Subscript(value=Attribute(value=Name(id='runner', ctx=Load()), attr='batch_metrics', ctx=Load()), slice=Constant(value='gradient/growth_tracker'), ctx=Store())], value=Subscript(value=Name(id='scaler_state', ctx=Load()), slice=Constant(value='_growth_tracker'), ctx=Load()))], orelse=[])], orelse=[])], decorator_list=[]), FunctionDef(name='_apply_gradnorm', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='runner')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='grad_clip_fn', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[If(test=Call(func=Name(id='hasattr', ctx=Load()), args=[Attribute(value=Name(id='runner', ctx=Load()), attr='engine', ctx=Load()), Constant(value='scaler')], keywords=[]), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Attribute(value=Name(id='runner', ctx=Load()), attr='engine', ctx=Load()), attr='scaler', ctx=Load()), attr='unscale_', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='optimizer', ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='norm', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='grad_clip_fn', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), attr='parameters', ctx=Load()), args=[], keywords=[])], keywords=[]))], orelse=[Assign(targets=[Name(id='parameters', ctx=Store())], value=ListComp(elt=Name(id='p', ctx=Load()), generators=[comprehension(target=Name(id='p', ctx=Store()), iter=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), attr='parameters', ctx=Load()), args=[], keywords=[]), ifs=[Compare(left=Attribute(value=Name(id='p', ctx=Load()), attr='grad', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)])], is_async=0)])), Assign(targets=[Name(id='device', ctx=Store())], value=Attribute(value=Attribute(value=Subscript(value=Name(id='parameters', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='grad', ctx=Load()), attr='device', ctx=Load())), Assign(targets=[Name(id='norm', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='norm', ctx=Load()), args=[Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='stack', ctx=Load()), args=[ListComp(elt=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='norm', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='p', ctx=Load()), attr='grad', ctx=Load()), attr='detach', ctx=Load()), args=[], keywords=[])], keywords=[]), attr='to', ctx=Load()), args=[Name(id='device', ctx=Load())], keywords=[]), generators=[comprehension(target=Name(id='p', ctx=Store()), iter=Name(id='parameters', ctx=Load()), ifs=[], is_async=0)])], keywords=[])], keywords=[]))]), Assign(targets=[Subscript(value=Attribute(value=Name(id='runner', ctx=Load()), attr='batch_metrics', ctx=Load()), slice=Constant(value='gradient/norm'), ctx=Store())], value=Call(func=Attribute(value=Name(id='norm', ctx=Load()), attr='item', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), FunctionDef(name='_closure', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='runner')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Forward-backward pass used in multi-step optimizers.')), Expr(value=Call(func=Attribute(value=Name(id='runner', ctx=Load()), attr='_handle_train_batch', ctx=Load()), args=[Tuple(elts=[Subscript(value=Attribute(value=Name(id='runner', ctx=Load()), attr='batch', ctx=Load()), slice=Constant(value='images'), ctx=Load()), Subscript(value=Attribute(value=Name(id='runner', ctx=Load()), attr='batch', ctx=Load()), slice=Constant(value='labels'), ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='runner', ctx=Load()), attr='batch', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='runner', ctx=Load()), attr='engine', ctx=Load()), attr='sync_device', ctx=Load()), args=[Attribute(value=Name(id='runner', ctx=Load()), attr='batch', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='runner', ctx=Load()), attr='callbacks', ctx=Load()), slice=Constant(value='criterion'), ctx=Load()), attr='on_batch_end', ctx=Load()), args=[Name(id='runner', ctx=Load())], keywords=[])), Assign(targets=[Name(id='loss', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='runner', ctx=Load()), attr='batch_metrics', ctx=Load()), slice=Attribute(value=Name(id='self', ctx=Load()), attr='metric_key', ctx=Load()), ctx=Load())), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='runner', ctx=Load()), attr='engine', ctx=Load()), attr='zero_grad', ctx=Load()), args=[Name(id='loss', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='optimizer', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='runner', ctx=Load()), attr='engine', ctx=Load()), attr='backward_loss', ctx=Load()), args=[Name(id='loss', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='optimizer', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_apply_gradnorm', ctx=Load()), args=[Name(id='runner', ctx=Load())], keywords=[])), Return(value=Name(id='loss', ctx=Load()))], decorator_list=[])], decorator_list=[]), ClassDef(name='ArcFace', bases=[Attribute(value=Attribute(value=Attribute(value=Name(id='catalyst', ctx=Load()), attr='contrib', ctx=Load()), attr='nn', ctx=Load()), attr='ArcFace', ctx=Load())], keywords=[], body=[FunctionDef(name='forward', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='input', annotation=Attribute(value=Name(id='torch', ctx=Load()), attr='Tensor', ctx=Load())), arg(arg='target', annotation=Attribute(value=Name(id='torch', ctx=Load()), attr='LongTensor', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Assign(targets=[Name(id='cos_theta', ctx=Store())], value=Call(func=Attribute(value=Name(id='F', ctx=Load()), attr='linear', ctx=Load()), args=[Call(func=Attribute(value=Name(id='F', ctx=Load()), attr='normalize', ctx=Load()), args=[Name(id='input', ctx=Load())], keywords=[]), Call(func=Attribute(value=Name(id='F', ctx=Load()), attr='normalize', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='weight', ctx=Load())], keywords=[])], keywords=[])), If(test=Compare(left=Name(id='target', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Return(value=BinOp(left=Name(id='cos_theta', ctx=Load()), op=Mult(), right=Attribute(value=Name(id='self', ctx=Load()), attr='s', ctx=Load())))], orelse=[]), Assign(targets=[Name(id='theta', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='acos', ctx=Load()), args=[Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='clamp', ctx=Load()), args=[Name(id='cos_theta', ctx=Load()), BinOp(left=UnaryOp(op=USub(), operand=Constant(value=1.0)), op=Add(), right=Attribute(value=Name(id='self', ctx=Load()), attr='eps', ctx=Load())), BinOp(left=Constant(value=1.0), op=Sub(), right=Attribute(value=Name(id='self', ctx=Load()), attr='eps', ctx=Load()))], keywords=[])], keywords=[])), Assign(targets=[Name(id='one_hot', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='zeros_like', ctx=Load()), args=[Name(id='cos_theta', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='one_hot', ctx=Load()), attr='scatter_', ctx=Load()), args=[Constant(value=1), Call(func=Attribute(value=Call(func=Attribute(value=Name(id='target', ctx=Load()), attr='view', ctx=Load()), args=[UnaryOp(op=USub(), operand=Constant(value=1)), Constant(value=1)], keywords=[]), attr='long', ctx=Load()), args=[], keywords=[]), Constant(value=1)], keywords=[])), Assign(targets=[Name(id='mask', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='where', ctx=Load()), args=[Compare(left=Name(id='theta', ctx=Load()), ops=[Gt()], comparators=[Attribute(value=Name(id='self', ctx=Load()), attr='threshold', ctx=Load())]), Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='zeros_like', ctx=Load()), args=[Name(id='one_hot', ctx=Load())], keywords=[]), Name(id='one_hot', ctx=Load())], keywords=[])), Assign(targets=[Name(id='logits', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='cos', ctx=Load()), args=[Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='where', ctx=Load()), args=[Call(func=Attribute(value=Name(id='mask', ctx=Load()), attr='bool', ctx=Load()), args=[], keywords=[]), BinOp(left=Name(id='theta', ctx=Load()), op=Add(), right=Attribute(value=Name(id='self', ctx=Load()), attr='m', ctx=Load())), Name(id='theta', ctx=Load())], keywords=[])], keywords=[])), AugAssign(target=Name(id='logits', ctx=Store()), op=Mult(), value=Attribute(value=Name(id='self', ctx=Load()), attr='s', ctx=Load())), Return(value=Name(id='logits', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='torch', ctx=Load()), attr='Tensor', ctx=Load()))], decorator_list=[]), ClassDef(name='CosFace', bases=[Attribute(value=Attribute(value=Attribute(value=Name(id='catalyst', ctx=Load()), attr='contrib', ctx=Load()), attr='nn', ctx=Load()), attr='CosFace', ctx=Load())], keywords=[], body=[FunctionDef(name='forward', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='input', annotation=Attribute(value=Name(id='torch', ctx=Load()), attr='Tensor', ctx=Load())), arg(arg='target', annotation=Attribute(value=Name(id='torch', ctx=Load()), attr='LongTensor', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Assign(targets=[Name(id='cosine', ctx=Store())], value=Call(func=Attribute(value=Name(id='F', ctx=Load()), attr='linear', ctx=Load()), args=[Call(func=Attribute(value=Name(id='F', ctx=Load()), attr='normalize', ctx=Load()), args=[Name(id='input', ctx=Load())], keywords=[]), Call(func=Attribute(value=Name(id='F', ctx=Load()), attr='normalize', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='weight', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='phi', ctx=Store())], value=BinOp(left=Name(id='cosine', ctx=Load()), op=Sub(), right=Attribute(value=Name(id='self', ctx=Load()), attr='m', ctx=Load()))), If(test=Compare(left=Name(id='target', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Return(value=BinOp(left=Name(id='cosine', ctx=Load()), op=Mult(), right=Attribute(value=Name(id='self', ctx=Load()), attr='s', ctx=Load())))], orelse=[]), Assign(targets=[Name(id='one_hot', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='zeros_like', ctx=Load()), args=[Name(id='cosine', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='one_hot', ctx=Load()), attr='scatter_', ctx=Load()), args=[Constant(value=1), Call(func=Attribute(value=Call(func=Attribute(value=Name(id='target', ctx=Load()), attr='view', ctx=Load()), args=[UnaryOp(op=USub(), operand=Constant(value=1)), Constant(value=1)], keywords=[]), attr='long', ctx=Load()), args=[], keywords=[]), Constant(value=1)], keywords=[])), Assign(targets=[Name(id='logits', ctx=Store())], value=BinOp(left=BinOp(left=Name(id='one_hot', ctx=Load()), op=Mult(), right=Name(id='phi', ctx=Load())), op=Add(), right=BinOp(left=BinOp(left=Constant(value=1.0), op=Sub(), right=Name(id='one_hot', ctx=Load())), op=Mult(), right=Name(id='cosine', ctx=Load())))), AugAssign(target=Name(id='logits', ctx=Store()), op=Mult(), value=Attribute(value=Name(id='self', ctx=Load()), attr='s', ctx=Load())), Return(value=Name(id='logits', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='torch', ctx=Load()), attr='Tensor', ctx=Load()))], decorator_list=[])], type_ignores=[])