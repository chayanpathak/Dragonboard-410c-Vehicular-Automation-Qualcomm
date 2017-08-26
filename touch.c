#include <stdio.h> 
#include <stdlib.h>
 
#include "libsoc_gpio.h"
#include "libsoc_debug.h"
 
#define GPIO_LED   13
#define GPIO_BUTTON  35   
 
int main()
{   int count=0;
    gpio *gpio_led,*gpio_button;
    libsoc_set_debug(1);
    gpio_led = libsoc_gpio_request(GPIO_LED,LS_GPIO_SHARED);
    gpio_button = libsoc_gpio_request(GPIO_BUTTON,LS_GPIO_SHARED);
    if((gpio_led == NULL) || (gpio_button == NULL))
    {
    goto fail;
    }
    libsoc_gpio_set_direction(gpio_led,OUTPUT);
    libsoc_gpio_set_direction(gpio_button,INPUT);
    if((libsoc_gpio_get_direction(gpio_led) != OUTPUT) 
    || (libsoc_gpio_get_direction(gpio_button) != INPUT))   
    {
    goto fail;
    }
    while(1)
    {
    int n = libsoc_gpio_get_level(gpio_button);
    if(n == HIGH)
    {   
        printf("\n Intruder alert !!!!\n\n");
        while(1)
        {
        libsoc_gpio_set_level(gpio_led,HIGH);
        sleep(1);
	printf("\a");
        libsoc_gpio_set_level(gpio_led,LOW);
        sleep(1);
        count++;
        n = libsoc_gpio_get_level(gpio_button);
        //if(count>5)
          // goto abc;
        if(n == HIGH)
            goto abc;
        if(count>5)
           { //printf("\n Owner has realised the theft \n\n");
	     libsoc_gpio_set_level(gpio_led,LOW);
             goto abc;       
           }
       // else
         //  { printf("\n Welcome, Qurious \n\n");
           //  libsoc_gpio_set_level(gpio_led,LOW);
            
             
            // goto abc;
	    
          // }}//break;
        }
    }
    libsoc_gpio_set_level(gpio_led,LOW);
    usleep(1000000);
    }

    fail:
    if(gpio_led || gpio_button)
    {
    printf("apply gpio resource fail!\n");
    libsoc_gpio_free(gpio_led);
    libsoc_gpio_free(gpio_button);
    }
  
abc:
    return count;
}
