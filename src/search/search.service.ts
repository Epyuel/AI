import { Injectable,Body, Req } from '@nestjs/common';
import { link } from 'fs';
import { PrismaService } from '../prisma/prisma.service';
import { SearchDto } from './dto';


@Injectable()
export class SearchService {
    constructor(private prisma:PrismaService){}

    async getpackages(@Body() dto){
        const pads= await this.prisma.search.findUnique({
            where:{
                title:dto.title,
                DepartureDate:dto.departureDate,  
            }
        })
        return pads;
    }

    async create(dto: SearchDto){
        return this.prisma.search.create({
            data:{
                title:dto.title,
                link:dto.link,
                DepartureDate:dto.departureDate,
            }
        })
    }
}
