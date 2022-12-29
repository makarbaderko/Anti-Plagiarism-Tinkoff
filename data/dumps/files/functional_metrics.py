Module(body=[ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='typing', names=[alias(name='Union')], level=0), Import(names=[alias(name='numpy', asname='np')]), Assign(targets=[Name(id='ArrayLike', ctx=Store())], value=Subscript(value=Name(id='List', ctx=Load()), slice=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='float', ctx=Load()), Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load())), FunctionDef(name='mape', args=arguments(posonlyargs=[], args=[arg(arg='y_true', annotation=Name(id='ArrayLike', ctx=Load())), arg(arg='y_pred', annotation=Name(id='ArrayLike', ctx=Load())), arg(arg='eps', annotation=Name(id='float', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=1e-15)]), body=[Expr(value=Constant(value='Mean absolute percentage error.\n\n    `Wikipedia entry on the Mean absolute percentage error\n    <https://en.wikipedia.org/wiki/Mean_absolute_percentage_error>`_\n\n    Parameters\n    ----------\n    y_true:\n        array-like of shape (n_samples,) or (n_samples, n_outputs)\n\n        Ground truth (correct) target values.\n\n    y_pred:\n        array-like of shape (n_samples,) or (n_samples, n_outputs)\n\n        Estimated target values.\n\n    eps: float=1e-15\n        MAPE is undefined for ``y_true[i]==0`` for any ``i``, so all zeros ``y_true[i]`` are\n        clipped to ``max(eps, abs(y_true))``.\n\n    Returns\n    -------\n    float\n        A non-negative floating point value (the best value is 0.0).\n    ')), Assign(targets=[Tuple(elts=[Name(id='y_true_array', ctx=Store()), Name(id='y_pred_array', ctx=Store())], ctx=Store())], value=Tuple(elts=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='asarray', ctx=Load()), args=[Name(id='y_true', ctx=Load())], keywords=[]), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='asarray', ctx=Load()), args=[Name(id='y_pred', ctx=Load())], keywords=[])], ctx=Load())), If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='y_true_array', ctx=Load()), attr='shape', ctx=Load())], keywords=[]), ops=[NotEq()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='y_pred_array', ctx=Load()), attr='shape', ctx=Load())], keywords=[])]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Shapes of the labels must be the same')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='y_true_array', ctx=Store())], value=Call(func=Attribute(value=Name(id='y_true_array', ctx=Load()), attr='clip', ctx=Load()), args=[Name(id='eps', ctx=Load())], keywords=[])), Return(value=BinOp(left=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='mean', ctx=Load()), args=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='abs', ctx=Load()), args=[BinOp(left=BinOp(left=Name(id='y_true_array', ctx=Load()), op=Sub(), right=Name(id='y_pred_array', ctx=Load())), op=Div(), right=Name(id='y_true_array', ctx=Load()))], keywords=[])], keywords=[]), op=Mult(), right=Constant(value=100)))], decorator_list=[], returns=Name(id='float', ctx=Load())), FunctionDef(name='smape', args=arguments(posonlyargs=[], args=[arg(arg='y_true', annotation=Name(id='ArrayLike', ctx=Load())), arg(arg='y_pred', annotation=Name(id='ArrayLike', ctx=Load())), arg(arg='eps', annotation=Name(id='float', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=1e-15)]), body=[Expr(value=Constant(value='Symmetric mean absolute percentage error.\n\n    `Wikipedia entry on the Symmetric mean absolute percentage error\n    <https://en.wikipedia.org/wiki/Symmetric_mean_absolute_percentage_error>`_\n\n    .. math::\n        SMAPE = \\dfrac{100}{n}\\sum_{t=1}^{n}\\dfrac{|ytrue_{t}-ypred_{t}|}{(|ypred_{t}|+|ytrue_{t}|) / 2}\n\n    Parameters\n    ----------\n    y_true:\n        array-like of shape (n_samples,) or (n_samples, n_outputs)\n\n        Ground truth (correct) target values.\n\n    y_pred:\n        array-like of shape (n_samples,) or (n_samples, n_outputs)\n\n        Estimated target values.\n\n    eps: float=1e-15\n        SMAPE is undefined for ``y_true[i] + y_pred[i] == 0`` for any ``i``, so all zeros ``y_true[i] + y_pred[i]`` are\n        clipped to ``max(eps, abs(y_true) + abs(y_pred))``.\n\n    Returns\n    -------\n    float\n        A non-negative floating point value (the best value is 0.0).\n    ')), Assign(targets=[Tuple(elts=[Name(id='y_true_array', ctx=Store()), Name(id='y_pred_array', ctx=Store())], ctx=Store())], value=Tuple(elts=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='asarray', ctx=Load()), args=[Name(id='y_true', ctx=Load())], keywords=[]), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='asarray', ctx=Load()), args=[Name(id='y_pred', ctx=Load())], keywords=[])], ctx=Load())), If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='y_true_array', ctx=Load()), attr='shape', ctx=Load())], keywords=[]), ops=[NotEq()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='y_pred_array', ctx=Load()), attr='shape', ctx=Load())], keywords=[])]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Shapes of the labels must be the same')], keywords=[]))], orelse=[]), Return(value=BinOp(left=Constant(value=100), op=Mult(), right=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='mean', ctx=Load()), args=[BinOp(left=BinOp(left=Constant(value=2), op=Mult(), right=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='abs', ctx=Load()), args=[BinOp(left=Name(id='y_pred_array', ctx=Load()), op=Sub(), right=Name(id='y_true_array', ctx=Load()))], keywords=[])), op=Div(), right=Call(func=Attribute(value=BinOp(left=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='abs', ctx=Load()), args=[Name(id='y_true_array', ctx=Load())], keywords=[]), op=Add(), right=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='abs', ctx=Load()), args=[Name(id='y_pred_array', ctx=Load())], keywords=[])), attr='clip', ctx=Load()), args=[Name(id='eps', ctx=Load())], keywords=[]))], keywords=[])))], decorator_list=[], returns=Name(id='float', ctx=Load())), FunctionDef(name='sign', args=arguments(posonlyargs=[], args=[arg(arg='y_true', annotation=Name(id='ArrayLike', ctx=Load())), arg(arg='y_pred', annotation=Name(id='ArrayLike', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Sign error metric.\n\n    .. math::\n        Sign(y\\_true, y\\_pred) = \\frac{1}{n}\\cdot\\sum_{i=0}^{n - 1}{sign(y\\_true_i - y\\_pred_i)}\n\n    Parameters\n    ----------\n    y_true:\n        array-like of shape (n_samples,) or (n_samples, n_outputs)\n\n        Ground truth (correct) target values.\n\n    y_pred:\n        array-like of shape (n_samples,) or (n_samples, n_outputs)\n\n        Estimated target values.\n\n    Returns\n    -------\n    float\n        A floating point value (the best value is 0.0).\n    ')), Assign(targets=[Tuple(elts=[Name(id='y_true_array', ctx=Store()), Name(id='y_pred_array', ctx=Store())], ctx=Store())], value=Tuple(elts=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='asarray', ctx=Load()), args=[Name(id='y_true', ctx=Load())], keywords=[]), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='asarray', ctx=Load()), args=[Name(id='y_pred', ctx=Load())], keywords=[])], ctx=Load())), If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='y_true_array', ctx=Load()), attr='shape', ctx=Load())], keywords=[]), ops=[NotEq()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='y_pred_array', ctx=Load()), attr='shape', ctx=Load())], keywords=[])]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Shapes of the labels must be the same')], keywords=[]))], orelse=[]), Return(value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='mean', ctx=Load()), args=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='sign', ctx=Load()), args=[BinOp(left=Name(id='y_true_array', ctx=Load()), op=Sub(), right=Name(id='y_pred_array', ctx=Load()))], keywords=[])], keywords=[]))], decorator_list=[], returns=Name(id='float', ctx=Load()))], type_ignores=[])