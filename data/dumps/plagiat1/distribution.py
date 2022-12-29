Module(body=[Expr(value=Constant(value='\nMIT LICENCE\n\nCopyright (c) 2016 Maximilian Christ, Blue Yonder GmbH\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\ndocumentation files (the "Software"), to deal in the Software without restriction, including without limitation the\nrights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit\npersons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the\nSoftware.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE\nWARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR\nCOPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR\nOTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n')), Import(names=[alias(name='warnings')]), FunctionDef(name='initialize_warnings_in_workers', args=arguments(posonlyargs=[], args=[arg(arg='show_warnings')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='catch_warnings', ctx=Load()), args=[], keywords=[])), If(test=UnaryOp(op=Not(), operand=Name(id='show_warnings', ctx=Load())), body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='simplefilter', ctx=Load()), args=[Constant(value='ignore')], keywords=[]))], orelse=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='simplefilter', ctx=Load()), args=[Constant(value='default')], keywords=[]))])], decorator_list=[])], type_ignores=[])