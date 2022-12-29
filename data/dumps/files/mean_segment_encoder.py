Module(body=[Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='etna.transforms', names=[alias(name='Transform')], level=0), ImportFrom(module='etna.transforms.base', names=[alias(name='FutureMixin')], level=0), ImportFrom(module='etna.transforms.math.statistics', names=[alias(name='MeanTransform')], level=0), ClassDef(name='MeanSegmentEncoderTransform', bases=[Name(id='Transform', ctx=Load()), Name(id='FutureMixin', ctx=Load())], keywords=[], body=[Expr(value=Constant(value="Makes expanding mean target encoding of the segment. Creates column 'segment_mean'.")), Assign(targets=[Name(id='idx', ctx=Store())], value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load())), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='mean_encoder', ctx=Store())], value=Call(func=Name(id='MeanTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='window', value=UnaryOp(op=USub(), operand=Constant(value=1))), keyword(arg='out_column', value=Constant(value='segment_mean'))])), AnnAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='global_means', ctx=Store()), annotation=Subscript(value=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load()), value=Constant(value=None), simple=0)], decorator_list=[]), FunctionDef(name='fit', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n        Fit encoder.\n\n        Parameters\n        ----------\n        df:\n            dataframe with data to fit expanding mean target encoder.\n\n        Returns\n        -------\n        :\n            Fitted transform\n        ')), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='mean_encoder', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='global_means', ctx=Store())], value=Attribute(value=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='idx', ctx=Load()), slice=Tuple(elts=[Slice(), Constant(value='target')], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), attr='mean', ctx=Load()), args=[], keywords=[]), attr='values', ctx=Load())), Return(value=Name(id='self', ctx=Load()))], decorator_list=[], returns=Constant(value='MeanSegmentEncoderTransform')), FunctionDef(name='transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n        Get encoded values for the segment.\n\n        Parameters\n        ----------\n        df:\n            dataframe with data to transform.\n\n        Returns\n        -------\n        :\n            result dataframe\n        ')), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='mean_encoder', ctx=Load()), attr='transform', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Assign(targets=[Name(id='segment', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[]), slice=Constant(value=0), ctx=Load())), Assign(targets=[Name(id='nan_timestamps', ctx=Store())], value=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='idx', ctx=Load()), slice=Tuple(elts=[Name(id='segment', ctx=Load()), Constant(value='target')], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), attr='isna', ctx=Load()), args=[], keywords=[]), ctx=Load()), attr='index', ctx=Load())), Assign(targets=[Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Name(id='nan_timestamps', ctx=Load()), Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='idx', ctx=Load()), slice=Tuple(elts=[Slice(), Constant(value='segment_mean')], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Store())], value=Attribute(value=Name(id='self', ctx=Load()), attr='global_means', ctx=Load())), Return(value=Name(id='df', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], decorator_list=[])], type_ignores=[])