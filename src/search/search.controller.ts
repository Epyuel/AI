import { Body, Controller,Get,Post, Req } from '@nestjs/common';
import { SearchService } from './search.service';
import { SearchDto } from './dto';
import express, {Request} from 'express';

@Controller('search')
export class SearchController {
    constructor(private sea:SearchService){} 
    @Post('get')
    getpackages(@Body() dto){
        return this.sea.getpackages(dto);
    }

    @Post('create')
    create(@Body() dto:SearchDto){
        return this.sea.create(dto);
    }
}
