#include <stdio.h>
#include <stdlib.h>
 
#include "libsoc_gpio.h"
#include "libsoc_debug.h"
 
#define GPIO_LED    13
#define GPIO_SKEW     36
 
int main()
{
    gpio *gpio_led,*gpio_skew;
    libsoc_set_debug(1);
    gpio_led = libsoc_gpio_request(GPIO_LED,LS_GPIO_SHARED);
    gpio_skew = libsoc_gpio_request(GPIO_SKEW,LS_GPIO_SHARED);
    if((gpio_led == NULL) || (gpio_skew == NULL))
    {
    goto fail;
    }
    libsoc_gpio_set_direction(gpio_led,OUTPUT);
    libsoc_gpio_set_direction(gpio_skew,INPUT);
    if((libsoc_gpio_get_direction(gpio_led) != OUTPUT) 
    || (libsoc_gpio_get_direction(gpio_skew) != INPUT))   
    {
    goto fail;
    }
    while(1)
    {
    int n = libsoc_gpio_get_level(gpio_skew);
    if(n == HIGH)
    {
        libsoc_gpio_set_level(gpio_led,HIGH);
    }
    else
    {
        libsoc_gpio_set_level(gpio_led,LOW);
    }
    sleep(1);
    }
    fail:
    if(gpio_led || gpio_skew)
    {
    printf("apply gpio resource fail!\n");
    libsoc_gpio_free(gpio_led);
    libsoc_gpio_free(gpio_skew);
    }
    return EXIT_SUCCESS;
 
}

