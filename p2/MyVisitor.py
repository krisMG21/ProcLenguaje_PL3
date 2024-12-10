from MiniBVisitor import MiniBVisitor


class MyVisitor(MiniBVisitor):
    def visitStatement(self, ctx):
        return visitChildren(ctx)

    # def visitLetStmt(self, ctx): ...
