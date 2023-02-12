import { Module } from '@nestjs/common';
import { BookmarkModule } from './bookmark/bookmark.module';
import { PrismaModule } from './prisma/prisma.module';
import { ConfigModule } from '@nestjs/config';
import { UserModule } from './user/user.module';
import { AuthModule } from './auth/auth.module';
import { SearchModule } from './search/search.module';





@Module({
  imports: [ConfigModule.forRoot({isGlobal:true}),AuthModule, BookmarkModule, PrismaModule, UserModule,SearchModule],
})
export class AppModule {}
