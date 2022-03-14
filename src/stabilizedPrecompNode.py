import nuke

def connectPrecompNodes(startPrecompNode,endPrecompNode):
    startPrecompNodeName = startPrecompNode.knob("name").value() 
    endPrecompNode['pin1'].setExpression(startPrecompNodeName+'.pin1.x',0)
    endPrecompNode['pin1'].setExpression(startPrecompNodeName+'.pin1.y',1)
    endPrecompNode['pin2'].setExpression(startPrecompNodeName+'.pin2.x',0)
    endPrecompNode['pin2'].setExpression(startPrecompNodeName+'.pin2.y',1)
    endPrecompNode['pin3'].setExpression(startPrecompNodeName+'.pin3.x',0)
    endPrecompNode['pin3'].setExpression(startPrecompNodeName+'.pin3.y',1)
    endPrecompNode['pin4'].setExpression(startPrecompNodeName+'.pin4.x',0)
    endPrecompNode['pin4'].setExpression(startPrecompNodeName+'.pin4.y',1)