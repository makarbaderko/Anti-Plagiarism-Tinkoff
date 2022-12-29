Module(body=[Import(names=[alias(name='warnings')]), ImportFrom(module='typing', names=[alias(name='Callable')], level=0), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='etna.datasets', names=[alias(name='set_columns_wide')], level=0), ImportFrom(module='etna.transforms.base', names=[alias(name='Transform')], level=0), ImportFrom(module='etna.transforms.utils', names=[alias(name='match_target_quantiles')], level=0), ClassDef(name='LambdaTransform', bases=[Name(id='Transform', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='``LambdaTransform`` applies input function for given series.')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='in_column', annotation=Name(id='str', ctx=Load())), arg(arg='transform_func', annotation=Subscript(value=Name(id='Callable', ctx=Load()), slice=Tuple(elts=[List(elts=[Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())], ctx=Load()), Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='inplace', annotation=Name(id='bool', ctx=Load())), arg(arg='out_column', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='inverse_transform_func', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Callable', ctx=Load()), slice=Tuple(elts=[List(elts=[Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())], ctx=Load()), Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True), Constant(value=None), Constant(value=None)]), body=[Expr(value=Constant(value='Init ``LambdaTransform``.\n\n        Parameters\n        ----------\n        in_column:\n            column to apply transform\n        out_column:\n            name of added column. If not given, use ``self.__repr__()``\n        transform_func:\n            function to transform data\n        inverse_transform_func:\n            inverse function of ``transform_func``\n        inplace:\n\n            * if `True`, apply transformation inplace to ``in_column``,\n\n            * if `False`, add column and apply transformation to ``out_column``\n\n        Warnings\n        --------\n        throws if `inplace=True` and ``out_column`` is initialized, transformation will be applied inplace\n\n        Raises\n        ------\n        Value error:\n            if `inplace=True` and ``inverse_transform_func`` is not defined\n        ')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Store())], value=Name(id='in_column', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Store())], value=Name(id='inplace', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='out_column', ctx=Store())], value=Name(id='out_column', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='transform_func', ctx=Store())], value=Name(id='transform_func', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='inverse_transform_func', ctx=Store())], value=Name(id='inverse_transform_func', ctx=Load())), If(test=BoolOp(op=And(), values=[Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Load()), Name(id='out_column', ctx=Load())]), body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='warn', ctx=Load()), args=[Constant(value='Transformation will be applied inplace, out_column param will be ignored')], keywords=[]))], orelse=[]), If(test=BoolOp(op=And(), values=[Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Load()), Compare(left=Name(id='inverse_transform_func', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)])]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='inverse_transform_func must be defined, when inplace=True')], keywords=[]))], orelse=[]), If(test=Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Load()), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='change_column', ctx=Store())], value=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load()))], orelse=[If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='out_column', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='change_column', ctx=Store())], value=Attribute(value=Name(id='self', ctx=Load()), attr='out_column', ctx=Load()))], orelse=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='change_column', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='__repr__', ctx=Load()), args=[], keywords=[]))])])], decorator_list=[]), FunctionDef(name='fit', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Fit preprocess method, does nothing in ``LambdaTransform`` case.\n\n        Parameters\n        ----------\n        df:\n            dataframe with data.\n\n        Returns\n        -------\n        result: ``LambdaTransform``\n        ')), Return(value=Name(id='self', ctx=Load()))], decorator_list=[], returns=Constant(value='LambdaTransform')), FunctionDef(name='transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Apply lambda transformation to series from df.\n\n        Parameters\n        ----------\n        df:\n            series to transform\n\n        Returns\n        -------\n        :\n            transformed series\n        ')), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='segments', ctx=Store())], value=Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Name(id='set', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[])], keywords=[])], keywords=[])), Assign(targets=[Name(id='features', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='transformed_features', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='transform_func', ctx=Load()), args=[Name(id='features', ctx=Load())], keywords=[])), If(test=Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Load()), body=[Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Name(id='set_columns_wide', ctx=Load()), args=[Name(id='result', ctx=Load()), Name(id='transformed_features', ctx=Load())], keywords=[keyword(arg='features_left', value=List(elts=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load())), keyword(arg='features_right', value=List(elts=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()))]))], orelse=[Assign(targets=[Attribute(value=Name(id='transformed_features', ctx=Load()), attr='columns', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='pd', ctx=Load()), attr='MultiIndex', ctx=Load()), attr='from_product', ctx=Load()), args=[List(elts=[Name(id='segments', ctx=Load()), List(elts=[Attribute(value=Name(id='self', ctx=Load()), attr='change_column', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[BinOp(left=List(elts=[Name(id='result', ctx=Load())], ctx=Load()), op=Add(), right=List(elts=[Name(id='transformed_features', ctx=Load())], ctx=Load()))], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Attribute(value=Name(id='result', ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))]))]), Return(value=Name(id='result', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='inverse_transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Apply inverse transformation to the series from df.\n\n        Parameters\n        ----------\n        df:\n            series to transform\n\n        Returns\n        -------\n        :\n            transformed series\n        ')), Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), If(test=Attribute(value=Name(id='self', ctx=Load()), attr='inverse_transform_func', ctx=Load()), body=[Assign(targets=[Name(id='features', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='transformed_features', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='inverse_transform_func', ctx=Load()), args=[Name(id='features', ctx=Load())], keywords=[])), Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Name(id='set_columns_wide', ctx=Load()), args=[Name(id='result_df', ctx=Load()), Name(id='transformed_features', ctx=Load())], keywords=[keyword(arg='features_left', value=List(elts=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load())), keyword(arg='features_right', value=List(elts=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()))])), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load()), ops=[Eq()], comparators=[Constant(value='target')]), body=[Assign(targets=[Name(id='segment_columns', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='result_df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[]), attr='tolist', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='quantiles', ctx=Store())], value=Call(func=Name(id='match_target_quantiles', ctx=Load()), args=[Call(func=Name(id='set', ctx=Load()), args=[Name(id='segment_columns', ctx=Load())], keywords=[])], keywords=[])), For(target=Name(id='quantile_column_nm', ctx=Store()), iter=Name(id='quantiles', ctx=Load()), body=[Assign(targets=[Name(id='features', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='quantile_column_nm', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='transformed_features', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='inverse_transform_func', ctx=Load()), args=[Name(id='features', ctx=Load())], keywords=[])), Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Name(id='set_columns_wide', ctx=Load()), args=[Name(id='result_df', ctx=Load()), Name(id='transformed_features', ctx=Load())], keywords=[keyword(arg='features_left', value=List(elts=[Name(id='quantile_column_nm', ctx=Load())], ctx=Load())), keyword(arg='features_right', value=List(elts=[Name(id='quantile_column_nm', ctx=Load())], ctx=Load()))]))], orelse=[])], orelse=[])], orelse=[]), Return(value=Name(id='result_df', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], decorator_list=[])], type_ignores=[])