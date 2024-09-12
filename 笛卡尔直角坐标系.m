%% 直角坐标图

clear,clc;

cir = input('输入阿基米德螺旋线的旋向（右旋为1，左旋为0）：');
r0 = input('输入阿基米德螺旋线的起始半径(单位cm)：');
landa_spp = input('输入阿基米德螺旋线的螺距(单位cm)：');

if cir == 0
    angle = linspace(0,32*pi,1000);
    r = r0 + landa_spp*angle/(2*pi);
    x = r.*cos(angle);
    y = r.*sin(angle);
    plot(x,y);
elseif cir == 1
    angle = linspace(0,-32*pi,1000);
    r = r0 + landa_spp*(-angle)/(2*pi);
    x = r.*cos(angle);
    y = r.*sin(angle);
    plot(x,y);
end

%   figure处理
xlabel('坐标x'), ylabel('坐标y');
if cir == 0
    title('直角坐标-左旋阿基米德螺旋线');
elseif cir == 1
    title('直角坐标-右旋阿基米德螺旋线');
end
grid on;
