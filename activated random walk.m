L=100;


random=zeros(2,L);
count=zeros(1,L);
for N=1:L
    for T=1:1000
for n=1:N
    n=n+1;
    a=rand();
    i=ceil(a*L);
 count(i)=count(i)+1;   
end

sum=0;
for i=1:L
    sum=sum+count(i);
end


for t=1:T
    t=t+1;
    for n=1:L
        a=rand();
        if count(n)>=2
        
        if a<0.5
        random(1,n)=1;
        random(2,n)=1;
        else if a>=0.5 && a<0.75
                random(1,n)=0;
                random(2,n)=2;
                else if a>=0.75
                random(1,n)=2;
                random(2,n)=0;
                    end
            end
        end
        else
            random(1,n)=0;random(2,n)=0;
        end
        
    end
    
     if count(1)>=2
        count(1)=count(1)-2+random(1,2)+random(2,L);
    else
            count(1)=count(1)+random(1,2)+random(2,L);
     end
     if count(L)>=2
        count(L)=count(L)-2+random(1,1)+random(2,L-1);
    else
            count(L)=count(L)+random(1,1)+random(2,L-1);
    end
    
    
   


    
    for i=2:L-1
    if count(i)>=2
        count(i)=count(i)-2+random(1,i+1)+random(2,i-1);
    else
            count(i)=count(i)+random(1,i+1)+random(2,i-1);
    end
    end
    
end

sum=0;
for i=1:L
    sum=sum+count(i);
end


active=0;
for i=1:L
    if count(i)>1
        active=active+1;
    end
end

if active==0
    break
end
    end
    scatter(N/L,T)
    hold on
end











            

