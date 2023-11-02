import matplotlib.pyplot as plt

def PlotFrame(Frame,axes,num_frame):
    
    #plotando eixo x do frame
    axes.plot([Frame[0,3],Frame[0,3]+Frame[0,0]],[Frame[1,3],Frame[1,3]+Frame[1,0]],[Frame[2,3],Frame[2,3]+Frame[2,0]],color='blue',linewidth=2)
    axes.text(Frame[0,3]+Frame[0,0], Frame[1,3]+Frame[1,0], Frame[2,3]+Frame[2,0], f"X[{num_frame}]", color='black')

    #plotando eixo y do frame 
    axes.plot([Frame[0,3],Frame[0,3]+Frame[0,1]],[Frame[1,3],Frame[1,3]+Frame[1,1]],[Frame[2,3],Frame[2,3]+Frame[2,1]],color='red',linewidth=2)
    axes.text(Frame[0,3]+Frame[0,1], Frame[1,3]+Frame[1,1], Frame[2,3]+Frame[2,1], f"Y[{num_frame}]", color='black')

    #plotando eixo z do frame
    axes.plot([Frame[0,3],Frame[0,3]+Frame[0,2]],[Frame[1,3],Frame[1,3]+Frame[1,2]],[Frame[2,3],Frame[2,3]+Frame[2,2]],color='green',linewidth=2)
    axes.text(Frame[0,3]+Frame[0,2], Frame[1,3]+Frame[1,2], Frame[2,3]+Frame[2,2], f"Z[{num_frame}]", color='black')
    
def PlotTransicaoAB(FrameA,FrameB,axes):
    axes.plot([FrameA[0,3],FrameB[0,3]],[FrameA[1,3],FrameB[1,3]],[FrameA[2,3],FrameB[2,3]],color='lightsalmon',linewidth=2)