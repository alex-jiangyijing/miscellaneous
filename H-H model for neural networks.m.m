clear; clf; 
% maximal conductance (in units of mS/cm^2); 1=K+, 2=Na+, 3=Leakage 
g(1)=36; g(2)=120; g(3)=0.3;%was 36 in stead of 40, was .3  
% equilibrium potential for ions 
E(1)=-12; E(2)=115; E(3)=10.613; 
% Initialization of variables 
%I_ext=0;  
V=0; x=zeros(1,3); x(3)=1; t_rec=0; 
% Time step for integration 
dt=0.01;%was .01 
% Integration with Euler method 

firings=[];%new addition 
diff01=0; 
diff12=0; 
V0=0; 
for t=0:dt:45%was 90 
   %if t==1; I_ext=10; end %turn on external current at t=10 
  % if t==11; I_ext=0;  end %turn off external current at t=40  
  % if t==50; I_ext=10;  end %turn off external current at t=40  
   %if t==70; I_ext=0;  end %turn off external current at t=40  
   % alpha functions used in the model 
   %following 4 lines are new 
   V0=V; 
   if t<=10
I_ext=-5.76;
else
    I_ext=0;
   end
    if ((diff12>0) && (diff01<0)) 
              firings=[firings; t, 1];%record the firing time and the number of corresponding firing neurons 
    end 
    
   alpha(1)=(10-V)/(100*(exp((10-V)/10)-1)); 
   alpha(2)=(25-V)/(10*(exp((25-V)/10)-1)); 
   alpha(3)=0.07*exp(-V/20); 
   % beta functions used in the model 
   beta(1)=0.125*exp(-V/80); 
   beta(2)=4*exp(-V/18); 
   beta(3)=1/(exp((30-V)/10)+1); 
   % time constant Tau_x and the equilibirum value x_infty 
   tau=1./(alpha+beta);% 3 equations 
   x_infty=alpha.*tau; % 3 equations 
   % Integration with the Euler method 
   x=(1-dt./tau).*x+dt./tau.*x_infty;% 3 equations 
   % Calculate actual conductance g with given n,m,h 
   gnmh(1)=g(1)*x(1)^4; 
   gnmh(2)=g(2)*x(2)^3*x(3); 
   gnmh(3)=g(3); 
   %The internal ion current 
   I=gnmh.*(V-E); % 3 equations 
   %Update the membrane voltage 
   V=V+dt*(I_ext-sum(I)); 
 
   %following 6 lines are new 
   diff12=diff01;   %diff12 = v(t-1)-v(t-2) 
   diff01=V-V0;     %diff01 = v(t-0)-v(t-1) 
    
%     if V>30 
%            t 
%     end 
         
   %Record some variables for plotting after equilibration 
   if t>=0; 
      t_rec=t_rec+1; 
      x_plot(t_rec)=t; 
      y_plot(t_rec)=V; 
   end 
end % the end of time loop 
firings 
plot(x_plot,y_plot); xlabel('Time'); ylabel('Voltage'); 
