Module(body=[Import(names=[alias(name='warnings')]), ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='etna.transforms.base', names=[alias(name='PerSegmentWrapper')], level=0), ImportFrom(module='etna.transforms.base', names=[alias(name='Transform')], level=0), ClassDef(name='_OneSegmentResampleWithDistributionTransform', bases=[Name(id='Transform', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='_OneSegmentResampleWithDistributionTransform resamples the given column using the distribution of the other column.')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='in_column', annotation=Name(id='str', ctx=Load())), arg(arg='distribution_column', annotation=Name(id='str', ctx=Load())), arg(arg='inplace', annotation=Name(id='bool', ctx=Load())), arg(arg='out_column', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n        Init _OneSegmentResampleWithDistributionTransform.\n\n        Parameters\n        ----------\n        in_column:\n            name of column to be resampled\n        distribution_column:\n            name of column to obtain the distribution from\n        inplace:\n\n            * if True, apply resampling inplace to in_column,\n\n            * if False, add transformed column to dataset\n\n        out_column:\n            name of added column. If not given, use ``self.__repr__()``\n        ')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Store())], value=Name(id='in_column', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='distribution_column', ctx=Store())], value=Name(id='distribution_column', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Store())], value=Name(id='inplace', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='out_column', ctx=Store())], value=Name(id='out_column', ctx=Load())), AnnAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='distribution', ctx=Store()), annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), value=Constant(value=None), simple=0)], decorator_list=[]), FunctionDef(name='_get_folds', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n        Generate fold number for each timestamp of the dataframe.\n\n        Here the ``in_column`` frequency gap is divided into the folds with the size of dataset frequency gap.\n        ')), Assign(targets=[Name(id='in_column_index', ctx=Store())], value=Attribute(value=Call(func=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load()), ctx=Load()), attr='dropna', ctx=Load()), args=[], keywords=[]), attr='index', ctx=Load())), If(test=BoolOp(op=Or(), values=[Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='in_column_index', ctx=Load())], keywords=[]), ops=[LtE()], comparators=[Constant(value=1)]), BoolOp(op=And(), values=[Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='in_column_index', ctx=Load())], keywords=[]), ops=[GtE()], comparators=[Constant(value=3)]), UnaryOp(op=Not(), operand=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='infer_freq', ctx=Load()), args=[Name(id='in_column_index', ctx=Load())], keywords=[]))])]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Can not infer in_column frequency!Check that in_column frequency is compatible with dataset frequency.')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='in_column_freq', ctx=Store())], value=BinOp(left=Subscript(value=Name(id='in_column_index', ctx=Load()), slice=Constant(value=1), ctx=Load()), op=Sub(), right=Subscript(value=Name(id='in_column_index', ctx=Load()), slice=Constant(value=0), ctx=Load()))), Assign(targets=[Name(id='dataset_freq', ctx=Store())], value=BinOp(left=Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='index', ctx=Load()), slice=Constant(value=1), ctx=Load()), op=Sub(), right=Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='index', ctx=Load()), slice=Constant(value=0), ctx=Load()))), Assign(targets=[Name(id='n_folds_per_gap', ctx=Store())], value=BinOp(left=Name(id='in_column_freq', ctx=Load()), op=FloorDiv(), right=Name(id='dataset_freq', ctx=Load()))), Assign(targets=[Name(id='n_periods', ctx=Store())], value=BinOp(left=BinOp(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[]), op=FloorDiv(), right=Name(id='n_folds_per_gap', ctx=Load())), op=Add(), right=Constant(value=2))), Assign(targets=[Name(id='in_column_start_index', ctx=Store())], value=Subscript(value=Name(id='in_column_index', ctx=Load()), slice=Constant(value=0), ctx=Load())), Assign(targets=[Name(id='left_tie_len', ctx=Store())], value=BinOp(left=Call(func=Name(id='len', ctx=Load()), args=[Subscript(value=Name(id='df', ctx=Load()), slice=Slice(upper=Name(id='in_column_start_index', ctx=Load())), ctx=Load())], keywords=[]), op=Sub(), right=Constant(value=1))), Assign(targets=[Name(id='right_tie_len', ctx=Store())], value=Call(func=Name(id='len', ctx=Load()), args=[Subscript(value=Name(id='df', ctx=Load()), slice=Slice(lower=Name(id='in_column_start_index', ctx=Load())), ctx=Load())], keywords=[])), Assign(targets=[Name(id='folds_for_left_tie', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='range', ctx=Load()), args=[BinOp(left=Name(id='n_folds_per_gap', ctx=Load()), op=Sub(), right=Name(id='left_tie_len', ctx=Load())), Name(id='n_folds_per_gap', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='folds_for_right_tie', ctx=Store())], value=Subscript(value=ListComp(elt=Name(id='fold', ctx=Load()), generators=[comprehension(target=Name(id='_', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='n_periods', ctx=Load())], keywords=[]), ifs=[], is_async=0), comprehension(target=Name(id='fold', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='n_folds_per_gap', ctx=Load())], keywords=[]), ifs=[], is_async=0)]), slice=Slice(upper=Name(id='right_tie_len', ctx=Load())), ctx=Load())), Return(value=BinOp(left=Name(id='folds_for_left_tie', ctx=Load()), op=Add(), right=Name(id='folds_for_right_tie', ctx=Load())))], decorator_list=[], returns=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='int', ctx=Load()), ctx=Load())), FunctionDef(name='fit', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n        Obtain the resampling frequency and distribution from ``distribution_column``.\n\n        Parameters\n        ----------\n        df:\n            dataframe with data to fit the transform.\n\n        Returns\n        -------\n        :\n        ')), Assign(targets=[Name(id='df', ctx=Store())], value=Subscript(value=Name(id='df', ctx=Load()), slice=List(elts=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='distribution_column', ctx=Load())], ctx=Load()), ctx=Load())), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='fold'), ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_folds', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='distribution', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=List(elts=[Constant(value='fold'), Attribute(value=Name(id='self', ctx=Load()), attr='distribution_column', ctx=Load())], ctx=Load()), ctx=Load()), attr='groupby', ctx=Load()), args=[Constant(value='fold')], keywords=[]), attr='sum', ctx=Load()), args=[], keywords=[]), attr='reset_index', ctx=Load()), args=[], keywords=[])), AugAssign(target=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='distribution', ctx=Load()), slice=Attribute(value=Name(id='self', ctx=Load()), attr='distribution_column', ctx=Load()), ctx=Store()), op=Div(), value=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='distribution', ctx=Load()), slice=Attribute(value=Name(id='self', ctx=Load()), attr='distribution_column', ctx=Load()), ctx=Load()), attr='sum', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='distribution', ctx=Load()), attr='rename', ctx=Load()), args=[], keywords=[keyword(arg='columns', value=Dict(keys=[Attribute(value=Name(id='self', ctx=Load()), attr='distribution_column', ctx=Load())], values=[Constant(value='distribution')])), keyword(arg='inplace', value=Constant(value=True))])), Assign(targets=[Attribute(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='distribution', ctx=Load()), attr='columns', ctx=Load()), attr='name', ctx=Store())], value=Constant(value=None)), Return(value=Name(id='self', ctx=Load()))], decorator_list=[], returns=Constant(value='_OneSegmentResampleWithDistributionTransform')), FunctionDef(name='transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n        Resample the `in_column` using the distribution of `distribution_column`.\n\n        Parameters\n        ----------\n        df\n            dataframe with data to transform.\n\n        Returns\n        -------\n        :\n            result dataframe\n        ')), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='fold'), ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_folds', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='reset_index', ctx=Load()), args=[], keywords=[]), attr='merge', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='distribution', ctx=Load())], keywords=[keyword(arg='on', value=Constant(value='fold'))]), attr='set_index', ctx=Load()), args=[Constant(value='timestamp')], keywords=[]), attr='sort_index', ctx=Load()), args=[], keywords=[])), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Attribute(value=Name(id='self', ctx=Load()), attr='out_column', ctx=Load()), ctx=Store())], value=BinOp(left=Call(func=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load()), ctx=Load()), attr='ffill', ctx=Load()), args=[], keywords=[]), op=Mult(), right=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='distribution'), ctx=Load()))), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='drop', ctx=Load()), args=[List(elts=[Constant(value='fold'), Constant(value='distribution')], ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))])), Return(value=Name(id='df', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], decorator_list=[]), ClassDef(name='ResampleWithDistributionTransform', bases=[Name(id='PerSegmentWrapper', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='ResampleWithDistributionTransform resamples the given column using the distribution of the other column.\n\n    Warning\n    -------\n    This transform can suffer from look-ahead bias. For transforming data at some timestamp\n    it uses information from the whole train part.\n    ')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='in_column', annotation=Name(id='str', ctx=Load())), arg(arg='distribution_column', annotation=Name(id='str', ctx=Load())), arg(arg='inplace', annotation=Name(id='bool', ctx=Load())), arg(arg='out_column', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True), Constant(value=None)]), body=[Expr(value=Constant(value='\n        Init ResampleWithDistributionTransform.\n\n        Parameters\n        ----------\n        in_column:\n            name of column to be resampled\n        distribution_column:\n            name of column to obtain the distribution from\n        inplace:\n\n            * if True, apply resampling inplace to in_column,\n\n            * if False, add transformed column to dataset\n\n        out_column:\n            name of added column. If not given, use ``self.__repr__()``\n        ')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Store())], value=Name(id='in_column', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='distribution_column', ctx=Store())], value=Name(id='distribution_column', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Store())], value=Name(id='inplace', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='out_column', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_out_column', ctx=Load()), args=[Name(id='out_column', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='transform', value=Call(func=Name(id='_OneSegmentResampleWithDistributionTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Name(id='in_column', ctx=Load())), keyword(arg='distribution_column', value=Name(id='distribution_column', ctx=Load())), keyword(arg='inplace', value=Name(id='inplace', ctx=Load())), keyword(arg='out_column', value=Attribute(value=Name(id='self', ctx=Load()), attr='out_column', ctx=Load()))]))]))], decorator_list=[]), FunctionDef(name='_get_out_column', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='out_column', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="Get the `out_column` depending on the transform's parameters.")), If(test=BoolOp(op=And(), values=[Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Load()), Name(id='out_column', ctx=Load())]), body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='warn', ctx=Load()), args=[Constant(value='Transformation will be applied inplace, out_column param will be ignored')], keywords=[]))], orelse=[]), If(test=Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Load()), body=[Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load()))], orelse=[]), If(test=Name(id='out_column', ctx=Load()), body=[Return(value=Name(id='out_column', ctx=Load()))], orelse=[]), Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='__repr__', ctx=Load()), args=[], keywords=[]))], decorator_list=[], returns=Name(id='str', ctx=Load()))], decorator_list=[])], type_ignores=[])